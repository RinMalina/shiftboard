# === Stage 13: Add file save support using a configurable path ===
# Project: ShiftBoard
def save_roster(roster, path="shiftboard.json"):
    """Persist the current roster to a JSON file."""
    import json
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"roster": roster, "roles": roles}, f, indent=2)
        print(f"Roster saved to {path}")
    except FileNotFoundError:
        pass
