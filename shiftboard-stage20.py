# === Stage 20: Add duplicate detection for newly created records ===
# Project: ShiftBoard
def check_duplicates(
    records,
    *,
    primary_key: tuple | None = None,
) -> list[dict]:
    """Return a list of duplicate record dicts (where more than one share the same key)."""
    if not records:
        return []
    if primary_key is None:
        key_func = lambda r: tuple(r.values())
    else:
        key_func = lambda r: tuple(
            str(r.get(k)) for k in primary_key
        )

    seen = {}
    for rec in records:
        key = key_func(rec)
        if key not in seen:
            seen[key] = []
        seen[key].append(rec)

    return [r for r_list in seen.values() if len(r_list) > 1]
