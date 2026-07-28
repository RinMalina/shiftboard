# === Stage 32: Add pagination helpers for long console output ===
# Project: ShiftBoard
import sys


def paginate(lines, width=80):
    """Print a list of text lines in chunks that fit within `width` characters."""
    if not lines:
        return
    current = ""
    for line in lines:
        test = current + "\n" + line if current else line
        if len(test) <= width or (current and "\n" in test):
            current = test
        else:
            sys.stdout.write(current + "\n")
            current = line
    if current:
        print()


def chunked_print(items, size=10):
    """Yield items in fixed-size chunks for iteration or display."""
    for i in range(0, len(items), size):
        yield items[i:i + size]
