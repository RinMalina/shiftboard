# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: ShiftBoard
def _parse_availability(raw: str) -> dict:
    """Parse availability string like 'Mon,Tue,Thu 9-17' into a dict."""
    entry = {}
    parts = raw.strip().split()
    days = parts[0].split(',')
    hours = parts[1].split('-')
    for day in days:
        entry[day] = (int(hours[0]), int(hours[1]))
    return entry


def _check_coverage(weekly_roster: dict, required: dict) -> dict:
    """Return dict of days where coverage falls short, with shortfall count."""
    shortfall = {}
    for day, req in required.items():
        covered = weekly_roster.get(day, 0)
        if covered < req:
            shortfall[day] = req - covered
    return shortfall


def _format_roster(weekly_roster: dict) -> str:
    """Format a weekly roster as a readable string."""
    lines = ["Shift Roster\n"]
    for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
        staff = weekly_roster.get(day, [])
        lines.append(f"{day}: {', '.join(staff) if staff else 'No staff'}")
    return '\n'.join(lines)
