# === Stage 45: Add restore from backup with validation ===
# Project: ShiftBoard
import json, os

def restore_from_backup(backup_path):
    if not backup_path.endswith('.json'):
        raise ValueError("Backup must be a .json file")
    with open(backup_path) as f:
        data = json.load(f)
    required_keys = {'users', 'shifts', 'roles'}
    missing = required_keys - set(data.keys())
    if missing:
        raise ValueError(f"Missing keys in backup: {missing}")
    return data

def validate_backup(backup_path):
    raw = json.load(open(backup_path))
    for table in ('users', 'shifts'):
        if not isinstance(raw.get(table), list) or len(raw[table]) == 0:
            raise ValueError(f"{table} must be a non-empty list")
    return True

def backup_and_restore():
    path = "backups/shiftboard.json"
    os.makedirs("backups", exist_ok=True)
    with open(path, 'w') as f: json.dump({'users': [], 'shifts': []}, f)
    data = restore_from_backup(path)
    validate_backup(path)
    return data
