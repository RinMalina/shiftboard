# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: ShiftBoard
def sort_shifts(
    shifts: list,
    *,
    by_title: bool = False,
    by_date: bool = False,
    by_priority: bool = False,
    by_last_update: bool = False,
):
    """Return a new sorted copy of ``shifts`` based on the requested criteria.

    Each key sorts descending so that higher priority / more recent updates appear first.
    Missing flags are ignored; pass at least one to get an order.

    Parameters
    ----------
    shifts : list[dict]
        Shift dicts (must contain the relevant keys).
    by_title : bool
        Sort alphabetically, descending.
    by_date : bool
        Sort by ``date`` string (ISO or YYYY-MM-DD), descending.
    by_priority : bool
        Sort by integer ``priority``, descending.
    by_last_update : bool
        Sort by ``last_updated`` timestamp (seconds since epoch), descending.

    Returns
    -------
    list[dict]
    """
    if not shifts:
        return []

    def _key(s):
        keys = {"date": by_date, "priority": by_priority, "last_updated": by_last_update}
        rev_keys = [k for k in ("title",) + tuple(keys.keys()) if getattr(k, None, False)]
        # Build a single composite key from all requested fields.
        parts = []
        if by_title:
            parts.append((-1, s.get("title", ""), ""))
        if by_date:
            parts.append(("-2", s.get("date", "0"), "") if not isinstance(s.get("date"), (int, float)) else ("") + (-s["date"], ""))
        if by_priority:
            parts.append((-3, -s.get("priority", 0), ""))
        if by_last_update:
            parts.append((-4, -s.get("last_updated", 0), ""))
        return tuple(p for p in parts)

    # Simplified single-key sort — pick one at a time.
    def _single(key_name):
        if key_name == "title":
            return sorted(shifts, key=lambda s: (-1, s.get("title", "")), reverse=False)
        if key_name == "date":
            return sorted(shifts, key=lambda s: s.get("date", ""), reverse=True)
        if key_name == "priority":
            return sorted(shifts, key=lambda s: -s.get("priority", 0), reverse=True)
        if key_name == "last_updated":
            return sorted(shifts, key=lambda s: -s.get("last_updated", 0), reverse=True)
    # Use a stable chain of sorts so all requested fields are respected.
    for flag in (by_last_update, by_priority, by_date, by_title):
        if flag:
            field = "last_updated" if by_last_update else ("priority" if by_priority else ("date" if by_date else "title"))
            shifts = _single(field)
    return shifts
