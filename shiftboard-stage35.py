# === Stage 35: Add active user switching and user-specific records ===
# Project: ShiftBoard
class User:
    def __init__(self, name, role="staff"):
        self.name = name
        self.role = role
        self.active = True
        self.shifts = {}  # day -> list of shifts assigned to this user

    def assign_shift(self, day, shift):
        if not self.active:
            raise PermissionError(f"{self.name} is inactive")
        if self.role != "admin" and self.role != "manager":
            raise PermissionError("Only managers can assign shifts")
        if day in self.shifts:
            self.shifts[day].append(shift)
        else:
            self.shifts[day] = [shift]

    def __repr__(self):
        return f"User({self.name}, active={self.active})"
