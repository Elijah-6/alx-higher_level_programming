#!/usr/bin/python3
# 1-write_file.py
"""Defines a text file-reading function."""


def append_write(filename="", text=""):
    """write_file: write a string to a file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)