# === Stage 24: Add grouped summaries by category or status ===
# Project: ShiftBoard
def grouped_summary(teams, categories=None):
    """Return a compact dict summarizing teams by category or status."""
    if categories is None:
        groups = {t.get('category', 'Uncategorized'): t for t in teams}
    else:
        groups = {}
        for cat in categories:
            sub = [t for t in teams if t.get('category') == cat]
            if sub:
                groups[cat] = sub
    return {k: v if isinstance(v, list) else [v] for k, v in groups.items()}
