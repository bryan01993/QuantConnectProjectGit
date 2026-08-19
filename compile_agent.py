"""
This module provides a simple agent to ensure that a given QuantConnect
algorithm can be compiled without syntax errors. The agent is designed to
work in any Python environment and doesn't require the full QuantConnect
Lean infrastructure. Instead, it focuses on checking that the Python file
is syntactically correct and can be compiled to byte‑code. This serves as
a preflight check before submitting code to the QuantConnect platform.

CLI Usage:
    poetry run python compile_agent.py <path/to/algorithm.py>
"""

from __future__ import annotations

import ast
import py_compile
import sys
import traceback
from typing import Optional, Tuple


def compile_quantconnect_algorithm(file_path: str) -> Tuple[bool, Optional[str]]:
    """Attempt to compile a QuantConnect algorithm located at ``file_path``.

    Parameters
    ----------
    file_path : str
        The path to the Python file containing the QuantConnect algorithm.

    Returns
    -------
    Tuple[bool, Optional[str]]
        A tuple of (success_boolean, error_message_or_traceback).
        If compilation succeeds: (True, None).
        If compilation fails: (False, error_details_string).
    """
    try:
        with open(file_path, "r", encoding="utf-8") as source_file:
            source_code = source_file.read()

        # Step 1: Parse AST to catch syntax errors
        ast.parse(source_code, filename=file_path)

        # Step 2: Compile to byte-code to verify syntax completeness
        py_compile.compile(file_path, doraise=True)

        return True, None

    except SyntaxError as syn_err:
        err_msg = (
            f"[SYNTAX ERROR] Compilation failed for '{file_path}':\n"
            f"  File '{syn_err.filename}', line {syn_err.lineno}, col {syn_err.offset}\n"
            f"    {syn_err.text.strip() if syn_err.text else ''}\n"
            f"  SyntaxError: {syn_err.msg}"
        )
        return False, err_msg
    except py_compile.PyCompileError as comp_err:
        err_msg = f"[COMPILE ERROR] PyCompile failed for '{file_path}': {comp_err}"
        return False, err_msg
    except Exception as exc:
        err_msg = f"[ERROR] Unexpected compilation error for '{file_path}': {exc}\n{traceback.format_exc()}"
        return False, err_msg


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[USAGE] poetry run python compile_agent.py <target_file.py>")
        sys.exit(2)

    target_path = sys.argv[1]
    success, error_details = compile_quantconnect_algorithm(target_path)

    if success:
        print(f"[OK] Compiled successfully: {target_path}")
        sys.exit(0)
    else:
        print(error_details, file=sys.stderr)
        sys.exit(1)