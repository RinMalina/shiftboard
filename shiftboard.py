# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: ShiftBoard
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Role:
    name: str
    max_shifts_per_week: int = 5
    required_coverage: float = 0.8


@dataclass
class StaffMember:
    name: str
    role: Role
    availability: list[str] = field(default_factory=list)


@dataclass
class Shift:
    day: str
    start_time: str
    end_time: str
    assigned_to: Optional[StaffMember] = None
