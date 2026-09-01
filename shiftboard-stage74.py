# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: ShiftBoard
def snapshot_before_after(before, after):
    """Return a dict of keys whose values differ between before and after."""
    diff = {}
    all_keys = set(before) | set(after)
    for key in all_keys:
        if before.get(key) != after.get(key):
            diff[key] = {
                "before": before.get(key),
                "after": after.get(key),
            }
    return diff
