# === Stage 44: Add backup creation for the data file ===
# Project: ShiftBoard
def create_backup(source_path, backup_dir="."):
    """Create a timestamped copy of the data file."""
    import shutil, os, datetime
    if not os.path.exists(source_path):
        print(f"Source file not found: {source_path}")
        return False
    os.makedirs(backup_dir, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{os.path.basename(source_path)}.bak_{ts}"
    dst = os.path.join(backup_dir, backup_name)
    shutil.copy2(source_path, dst)
    print(f"Backup saved: {dst}")
    return True

if __name__ == "__main__":
    create_backup("shiftboard_data.json")
