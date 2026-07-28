# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: ShiftBoard
class Settings:
    def __init__(self):
        self.max_shifts_per_day = 2
        self.min_coverage_per_shift = 0
        self.weekly_roster_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        self.staff_role_required = False

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

    @classmethod
    def from_dict(cls, d):
        s = cls()
        for k, v in d.items():
            setattr(s, k, v)
        return s

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise ValueError(f"Unknown setting: {key}")
