# === Stage 60: Add saved views for frequently used filters ===
# Project: ShiftBoard
import json, os

DB_PATH = "shiftboard_data.json"

def save_view(view_name, filters):
    with open(DB_PATH, "a") as f:
        f.write(json.dumps({"view": view_name, "filters": filters}) + "\n")

def load_views():
    views = []
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    views.append(json.loads(line))
    return views
