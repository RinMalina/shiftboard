# === Stage 22: Add favorite records and quick favorite listing ===
# Project: ShiftBoard
def is_favorited(self, record_id: str) -> bool:
    """Check if a shift record has been marked as favorite."""
    return record_id in self._favorites

def mark_favorite(self, record_id: str) -> None:
    """Mark a shift record as favorite."""
    self._favorites.add(record_id)

def get_favorites(self) -> list[dict]:
    """Return all favorited records sorted by creation time (newest first)."""
    return [self._records[r] for r in sorted(self._favorites, key=lambda rid: self._record_times.get(rid, 0), reverse=True)]

def _save_favorites(self) -> None:
    """Persist favorites to disk alongside main data."""
    with open(self._db_path, 'w') as f:
        for line in self._lines:
            if isinstance(line, dict):
                f.write('F\n' + json.dumps(line, sort_keys=True))
            else:
                f.write(line)
