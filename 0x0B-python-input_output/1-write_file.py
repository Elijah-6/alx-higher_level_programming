#!/usr/bin/python3
# 1-write_file.py
"""Defines a text file-reading function."""


def write_file(filename="", text=""):
    """write_file: write a string to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)