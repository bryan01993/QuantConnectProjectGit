---
name: quantconnect-compiler
description: Triggers when the user or agent needs to compile, validate, or verify a QuantConnect algorithm/module's syntax before cloud submission.
---

# QuantConnect Algorithm Compilation & Validation Skill

Use this skill to compile and validate the syntax of Python files in this project (specifically QuantConnect algorithms and their helper modules). This is a critical pre-flight check for the **Code Agent** before pushing scripts to the QuantConnect Cloud.

## Execution Guidelines
- Before declaring any code edits or feature additions complete, verify that the modified file compiles successfully.
- Trigger the compilation using the standard script:
  `poetry run python compile_agent.py <file_path>`
- If compilation fails, analyze the syntax errors, resolve missing imports or syntax mismatches, and fix them before finalization.

## Research Directives
- **DD (Deep Dive)**: When compilation fails with complex type or syntax errors, perform a deep inspection of type definitions in `Docu/combined_documentation.pyi` and resolve the root cause.
- **ASAP (As Soon As Possible)**: Apply direct, surgical fixes to syntax or import bugs without altering trading logic architecture.
- **Single Algorithm Focus**: Keep syntax verification scoped strictly to the active strategy (e.g. `4_EarningsVolatilityCrunch/main.py`).
