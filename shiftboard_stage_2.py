# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: ShiftBoard
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Role:
    name: str
    min_covered: int = 1
    max_shifts: int = 5


@dataclass
class Availability:
    day: str          # 'Mon', 'Tue', ...
    start: str        # HH:MM
    end: str          # HH:MM
    required: bool = False

    def overlaps(self, other: "Availability") -> bool:
        s1, e1 = self.to_minutes(), self.end_to_minutes()
        s2, e2 = other.to_minutes(), other.end_to_minutes()
        return not (e1 <= s2 or e2 <= s1)

    @staticmethod
    def to_minutes(t: str) -> int:
        h, m = map(int, t.split(":"))
        return h * 60 + m


@dataclass
class ShiftRequest:
    slot_id: str
    role_name: str
    requested_by: Optional[str] = None
    status: str = "PENDING"   # PENDING | APPROVED | REJECTED

    def __repr__(self):
        return f"<ShiftRequest {self.slot_id} [{self.role_name}] -> {self.status}>"


@dataclass
class WeeklyRosterEntry:
    slot_id: str
    assigned_to: Optional[str] = None
    role_name: Optional[str] = None
    notes: str = ""

    def is_open(self) -> bool:
        return self.assigned_to is None
