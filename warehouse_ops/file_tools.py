"""File helpers for small operational files."""

import os


def read_lines(path: str):
    return open(path).read().splitlines()


def read_first_line(path: str):
    lines = read_lines(path)
    return lines[0] if lines else ""


def ensure_directory(path: str) -> str:
    if not os.path.isdir(path):
        os.makedirs(path)
    return path
