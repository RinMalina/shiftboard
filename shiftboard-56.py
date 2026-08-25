# === Stage 56: Add compact error classes for domain failures ===
# Project: ShiftBoard
class ShiftBoardError(Exception):
    """Base exception for all ShiftBoard domain failures."""
    pass


class RoleNotFoundError(ShiftBoardError):
    """Raised when a referenced role does not exist."""
    pass


class AvailabilityConflict(ShiftBoardError):
    """Raised when a requested shift conflicts with existing availability."""
    pass


class SwapRejected(ShiftBoardError):
    """Raised when a swap request cannot be applied (e.g. both parties busy)."""
    pass


class CoverageFailure(ShiftBoardError):
    """Raised when a shift request cannot be fulfilled (no available staff)."""
    pass


class SchedulerExhausted(ShiftBoardError):
    """Raised when all staff are booked and no further shifts can be scheduled."""
    pass
