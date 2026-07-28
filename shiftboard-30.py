# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: ShiftBoard
def parse_date(date_string):
    """Parse a date string in DD/MM/YYYY or YYYY-MM-DD format and return a datetime.date object."""
    for fmt in ('%d/%m/%Y', '%Y-%m-%d'):
        try:
            return datetime.strptime(date_string, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Invalid date string '{date_string}'. Use DD/MM/YYYY or YYYY-MM-DD format.")

def parse_date_range(start_string, end_string):
    """Parse a start and end date string and return (start_date, end_date) as datetime.date objects."""
    if not isinstance(start_string, str) or not isinstance(end_string, str):
        raise ValueError("Both arguments must be strings in DD/MM/YYYY or YYYY-MM-DD format.")
    try:
        start = parse_date(start_string)
    except ValueError as e:
        raise ValueError(f"Invalid start date '{start_string}': {e}") from None
    try:
        end = parse_date(end_string)
    except ValueError as e:
        raise ValueError(f"Invalid end date '{end_string}': {e}") from None
    if end < start:
        raise ValueError("End date must be after or equal to the start date.")
    return start, end

def is_valid_date_format(date_string):
    """Check if a string matches DD/MM/YYYY or YYYY-MM-DD format without raising exceptions."""
    try:
        parse_date(date_string)
        return True
    except ValueError:
        return False
