# === Stage 43: Add CSV import for the primary record type ===
# Project: ShiftBoard
import csv


def load_csv(filepath):
    """Read a CSV file and return rows as list of dicts."""
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
