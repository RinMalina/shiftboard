# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: ShiftBoard
def normalize_shift(shift: str | None) -> str | None:
    """Trim and lowercase a shift label for consistent lookup."""
    if not shift:
        return None
    return shift.strip().lower()


def parse_date(date_str: str | None) -> datetime.date:
    """Convert a 'YYYY-MM-DD' string to a date, returning None on failure."""
    if not date_str:
        return None
    try:
        return datetime.date.fromisoformat(date_str)
    except ValueError:
        return None


def parse_datetime(dt_str: str | None) -> datetime.datetime | None:
    """Convert a 'YYYY-MM-DD HH:MM' string to a datetime, returning None on failure."""
    if not dt_str:
        return None
    try:
        return datetime.datetime.fromisoformat(dt_str)
    except ValueError:
        return None


def chunk_list(lst: list, size: int) -> list[list]:
    """Split a list into chunks of *size* elements."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def pairwise(lst: list) -> list[tuple]:
    """Return overlapping pairs of elements (a, b) from *lst*."""
    return [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]


def is_valid_date_range(start: datetime.date, end: datetime.date) -> bool:
    """Return True if *start* and *end* form a non-empty date range."""
    if not isinstance(start, datetime.date) or not isinstance(end, datetime.date):
        return False
    return start <= end


def clamp(value: int, low: int, high: int) -> int:
    """Return *value* constrained to the inclusive range [*low*, *high*]."""
    return max(low, min(high, value))


def format_datetime(dt: datetime.datetime) -> str:
    """Format a datetime as 'YYYY-MM-DD HH:MM'."""
    return dt.strftime("%Y-%m-%d %H:%M")


def format_date(d: datetime.date) -> str:
    """Format a date as 'YYYY-MM-DD'."""
    return d.strftime("%Y-%m-%d")
