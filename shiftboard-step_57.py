# === Stage 57: Add structured result objects for command handlers ===
# Project: ShiftBoard
class ShiftResult:
    def __init__(self, status: str, message: str, data=None):
        self.status = status
        self.message = message
        self.data = data

    def to_dict(self):
        d = {"status": self.status, "message": self.message}
        if self.data is not None:
            d["data"] = self.data
        return d

    def __repr__(self):
        return f"ShiftResult({self.status}: {self.message})"
