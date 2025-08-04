"""
This module provides a simple agent to ensure that a given QuantConnect
algorithm can be compiled without syntax errors. The agent is designed to
work in any Python environment and doesn't require the full QuantConnect
Lean infrastructure. Instead, it focuses on checking that the Python file
is syntactically correct and can be compiled to byte‑code. This serves as
a preflight check before submitting code to the QuantConnect platform.

Functions
---------
compile_quantconnect_algorithm(file_path: str) -> bool
    Try to compile the algorithm located at ``file_path``. Return ``True``
    if the compilation succeeds, ``False`` otherwise.

Notes
-----
The function uses the built‑in ``ast`` and ``py_compile`` modules to
perform a basic compilation. It first parses the source code into an
abstract syntax tree (AST) and then attempts to compile it into
byte‑code. If either step raises a ``SyntaxError`` or a
``py_compile.PyCompileError``, the function returns ``False``. Any other
unexpected exception also results in a ``False`` return value. This
behavior ensures that the caller receives a boolean result without the
need to catch exceptions.

Example
-------
>>> result = compile_quantconnect_algorithm('path/to/algorithm.py')
>>> if result:
...     print("Algorithm compiled successfully!")
... else:
...     print("Compilation failed.")

"""

from __future__ import annotations

import ast
import py_compile
from typing import Optional


def compile_quantconnect_algorithm(file_path: str) -> bool:
    """Attempt to compile a QuantConnect algorithm located at ``file_path``.

    This function performs a two‑step compilation process:

    1. It uses ``ast.parse`` to ensure the source code is syntactically
       valid Python. This step does not execute the code and therefore
       doesn't require any external dependencies that the algorithm might
       import (e.g., QuantConnect's ``QCAlgorithm`` or ``AlgorithmImports``).
    2. It calls ``py_compile.compile`` with ``doraise=True`` to produce
       byte‑code. If the code is syntactically correct, this step will
       succeed regardless of missing imports because Python compiles
       modules lazily.

    Parameters
    ----------
    file_path : str
        The path to the Python file containing the QuantConnect algorithm.

    Returns
    -------
    bool
        ``True`` if the file compiles successfully, ``False`` otherwise.

    Notes
    -----
    This function does not catch or report specific error messages. It is
    intended to be a simple yes/no check. For detailed error reporting,
    callers should wrap this function and capture exceptions explicitly.
    """

    try:
        # Read the entire source file. Using UTF‑8 ensures that most files
        # containing non‑ASCII characters are handled correctly.
        with open(file_path, "r", encoding="utf-8") as source_file:
            source_code = source_file.read()

        # Parse the source code into an abstract syntax tree. This will
        # raise ``SyntaxError`` for invalid Python syntax.
        ast.parse(source_code)

        # Attempt to compile the file into byte‑code. The ``doraise=True``
        # flag instructs ``py_compile`` to raise an exception rather than
        # writing the compiled file. This avoids side effects on disk.
        py_compile.compile(file_path, doraise=True)

        # If both steps succeed, return True.
        return True

    except (SyntaxError, py_compile.PyCompileError):
        # A syntax error or compilation error occurred. Return False to
        # indicate failure.
        return False
    except Exception:
        # Catch any other unexpected exception and treat it as a failure.
        # In a production system, logging could be added here.
        return False