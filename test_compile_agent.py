"""
Unit tests for the ``compile_quantconnect_algorithm`` function.

These tests verify that the agent can correctly identify whether a
Python file is syntactically valid. They cover both success and failure
scenarios using temporary files created on the fly. The tests are
designed to run with ``pytest``, but any test runner that supports
standard ``assert`` statements will work.
"""

from __future__ import annotations

import os
import tempfile
import textwrap
from typing import Tuple

import pytest

from compile_agent import compile_quantconnect_algorithm


def _create_temp_file(contents: str) -> Tuple[str, str]:
    """Helper function to create a temporary file with given contents.

    Parameters
    ----------
    contents : str
        The text to write into the temporary file.

    Returns
    -------
    Tuple[str, str]
        A tuple containing the path to the temporary file and its name.

    Notes
    -----
    The caller is responsible for deleting the file after use.
    """
    fd, path = tempfile.mkstemp(suffix=".py")
    with os.fdopen(fd, "w", encoding="utf-8") as tmp_file:
        tmp_file.write(contents)
    name = os.path.basename(path)
    return path, name


def test_compile_valid_algorithm() -> None:
    """Test that a syntactically valid Python file compiles successfully."""
    # A minimal valid algorithm. The import is non‑existent in this test
    # environment, but that is acceptable because compilation does not
    # require imports to resolve when using ``py_compile``.
    code = textwrap.dedent(
        """
        from AlgorithmImports import *  # pretend QuantConnect import

        class DummyAlgorithm:
            def __init__(self):
                self.value = 42

            def run(self):
                return self.value
        """
    )
    path, name = _create_temp_file(code)

    try:
        result = compile_quantconnect_algorithm(path)
        assert result is True, f"Expected compilation to succeed for {name}"
    finally:
        os.remove(path)


def test_compile_invalid_algorithm() -> None:
    """Test that an invalid Python file is reported as failing compilation."""
    # This file has a syntax error: missing colon after function name.
    code = textwrap.dedent(
        """
        def broken_function()
            return None
        """
    )
    path, name = _create_temp_file(code)

    try:
        result = compile_quantconnect_algorithm(path)
        assert result is False, f"Expected compilation to fail for {name}"
    finally:
        os.remove(path)