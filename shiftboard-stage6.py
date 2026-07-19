# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: ShiftBoard
def delete_entry(store, key, confirm=False):
    """Remove a key from store if it exists and (optionally) user confirms."""
    if key in store:
        value = store.pop(key)
        if not confirm:
            print(f"⚠️  Deleted {key} without confirmation.")
        else:
            print(f"✅ Confirmed deletion of {key}.")
