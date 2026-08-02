# === Stage 46: Add a schema version field and migration helper ===
# Project: ShiftBoard
import json, os

SCHEMA_VERSION = 46

def migrate(db_path):
    if db_path.endswith('.json'):
        with open(db_path) as f:
            data = json.load(f)
    else:
        with open(db_path + '.db', 'rb') as f:
            import sqlite3
            conn = sqlite3.connect(f)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='shiftboard'")
            rows = cursor.fetchall()
            if not rows:
                return 0
            schema = cursor.execute(
                "SELECT sql FROM sqlite_master WHERE type='table' AND name='shiftboard'"
            ).fetchone()[0]
        conn.close()

    if isinstance(data, dict):
        data['_schema_version'] = SCHEMA_VERSION
        with open(db_path, 'w') as f:
            json.dump(data, f, indent=2)
        return 1
    else:
        return 0
