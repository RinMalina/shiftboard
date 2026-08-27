# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: ShiftBoard
def bulk_delete(self, shifts, confirmed=False):
        if not confirmed:
            raise PermissionError("Bulk delete requires explicit confirmation.")
        for shift in shifts:
            self._shifts.remove(shift)
        self._coverage = self._compute_coverage()
