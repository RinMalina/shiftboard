# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: ShiftBoard
def upcoming_reminders(items, now=None):
    """Return sorted list of (item, days_until) for items due after *now*."""
    if now is None:
        import datetime as _dt; now = _dt.datetime.now()
    results = []
    for label, target_date in items:
        if isinstance(target_date, str):
            target_date = _dt.datetime.strptime(target_date, "%Y-%m-%d")
        delta = (target_date - now).days
        if 0 < delta <= 30:
            results.append((label, delta))
    return sorted(results, key=lambda x: x[1])

def remind_upcoming(reminders):
    """Print a one-line reminder for each upcoming item."""
    next_items = upcoming_reminders(reminders)
    if not next_items:
        print("No upcoming reminders.")
        return
    print("Upcoming reminders:")
    for label, days in next_items:
        print(f"  - {label} in {days} day{'s' if days != 1 else ''}")

if __name__ == "__main__":
    remind_upcoming([("Shift swap", "2025-04-25"), ("Roster review", "2025-04-30")])
