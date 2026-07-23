# === Stage 18: Add an activity log with timestamps and action names ===
# Project: ShiftBoard
class ActivityLog:
    def __init__(self):
        self._entries = []

    @property
    def entries(self):
        return list(self._entries)

    def log(self, action: str, detail: str = "") -> "ActivityEntry":
        entry = ActivityEntry(timestamp=time(), action=action, detail=detail)
        self._entries.append(entry)
        return entry


class ActivityEntry:
    __slots__ = ("timestamp", "action", "detail")

    def __init__(self, timestamp: datetime, action: str, detail: str):
        self.timestamp = timestamp
        self.action = action
        self.detail = detail

    def __repr__(self):
        return f"<ActivityEntry ts={self.timestamp} action='{self.action}' {self.detail}>"
