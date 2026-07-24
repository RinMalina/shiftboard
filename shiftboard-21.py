# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: ShiftBoard
def archive_and_restore(self):
    """Move records older than a threshold to an archive list, and restore them if requested."""
    cutoff = self._config.get("archive_cutoff_days", 30)
    now = datetime.now()
    archived = [r for r in self.records if (now - r["created_at"]).days > cutoff]
    remaining = [r for r in self.records if r not in archived]
    self.records = remaining
    self._archive_log.append({"archived": len(archived), "restored": 0, "timestamp": now.isoformat()})
    return {"active_count": len(self.records), "archived_in_history": len(archived)}

def restore_from_archive(self):
    """Re-add all previously archived records to the active roster."""
    restored = []
    for entry in reversed(self._archive_log):
        if entry.get("restored") == 0 and entry["timestamp"] < now.isoformat():
            count, new_records = self._restore_batch(entry)
            restored.extend(new_records)
    return {"restored_count": len(restored), "active_count": len(self.records)}

def _restore_batch(self, entry):
    """Reconstruct records from a single archive log entry."""
    cutoff = datetime.fromisoformat(entry["timestamp"]) + timedelta(days=self._config.get("archive_cutoff_days", 30))
    new_records = []
    for r in self.records:
        if (datetime.now() - r["created_at"]).days <= cutoff.days and r not in new_records:
            new_records.append(r)
    return len(new_records), new_records

def get_archive_status(self):
    """Return summary of archived records and restoration history."""
    total_archived = sum(e.get("archived", 0) for e in self._archive_log)
    total_restored = sum(e.get("restored", 0) for e in self._archive_log)
    return {"total_archived": total_archived, "total_restored": total_restored, "current_active": len(self.records)}
