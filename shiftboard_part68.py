# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: ShiftBoard
def generate_changelog(activity_log, max_entries=20):
    """Generate a compact changelog from the activity log."""
    entries = []
    for date, changes in activity_log.items():
        for change in changes:
            entry = f"  - {change} ({date})"
            if entry not in entries:
                entries.append(entry)
            if len(entries) >= max_entries:
                break
        if len(entries) >= max_entries:
            break
    if not entries:
        return "  No changes recorded."
    return "  Changelog:\n" + "\n".join(entries[:max_entries])
