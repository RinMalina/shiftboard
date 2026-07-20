# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: ShiftBoard
def search_shifts(query, shifts):
    if not query:
        return shifts
    q = query.strip().lower()
    q = re.sub(r'[^a-z0-9\s]', '', q)
    matches = []
    for s in shifts:
        def _matches(field):
            val = getattr(s, field, '')
            if isinstance(val, str):
                return q in val.lower()
            elif isinstance(val, (list, tuple)):
                return any(q in item.lower() for item in val)
            else:
                return False

        fields = ['name', 'role', 'shift_id', 'start_time', 'end_time',
                  'coverage_status', 'swap_notes']
        if all(_matches(f) for f in fields):
            matches.append(s)
    return matches
