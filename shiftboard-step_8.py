# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: ShiftBoard
def filter_by_criteria(self, status=None, category=None, owner=None, tags=None):
    """Filter active boards by optional criteria."""
    results = []
    for board in self._boards.values():
        if status is not None and board.status != status:
            continue
        if category is not None and board.category != category:
            continue
        if owner is not None and board.owner != owner:
            continue
        if tags is not None:
            if not all(tag in board.tags for tag in tags):
                continue
        results.append(board)
    return results
