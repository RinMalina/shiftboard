# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: ShiftBoard
def load_json(path):
    """Read a JSON file with forgiving error handling."""
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Malformed JSON in {path}: {e.msg} at line {e.lineno}, column {e.colno}")
        return None
