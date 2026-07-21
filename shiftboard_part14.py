# === Stage 14: Add file load support with fallback demo data ===
# Project: ShiftBoard
def load_data(file_path=None):
    """Load shift data from JSON file, falling back to demo data if missing."""
    import json, os, sys
    if file_path and os.path.isfile(file_path):
        try:
            with open(file_path) as f:
                return json.load(f)
        except Exception:
            pass
    print("No file found; using built-in demo data.")
    return {
        "roles": ["Nurse", "Admin"],
        "staff": [
            {"name": "Alice", "role": "Nurse"},
            {"name": "Bob", "role": "Admin"},
            {"name": "Charlie", "role": "Nurse"}
        ],
        "shifts": [
            {"day": "Monday", "time": "08:00-16:00", "staff": [], "role": "Nurse"},
            {"day": "Tuesday", "time": "08:00-16:00", "staff": ["Alice"], "role": "Admin"}
        ]
    }
