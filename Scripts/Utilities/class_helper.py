"""
class_helper.py
===============
Class reflection and introspection helper.
"""

from __future__ import annotations

import inspect

def inspect_class_members(cls):
    return inspect.getmembers(cls)

if __name__ == "__main__":
    print("[ClassHelper] Ready.")
