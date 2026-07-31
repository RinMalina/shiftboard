# === Stage 41: Add plain text import for a simple line-based format ===
# Project: ShiftBoard
def import_plain_text(filename: str) -> list[dict]:
    """Import shifts from a simple line-based text format."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    shifts = []
    for line in lines:
        if not line.strip():
            continue
        parts = line.split(',')
        shift_type = parts[0].strip().lower()
        date = parts[1].strip()
        start_time = parts[2].strip()
        end_time = parts[3].strip()
        staff_name = parts[4].strip()
        role = parts[5].strip() if len(parts) > 5 else 'General'
        shifts.append({
            'type': shift_type,
            'date': date,
            'start': start_time,
            'end': end_time,
            'staff_name': staff_name,
            'role': role
        })
    return shifts
