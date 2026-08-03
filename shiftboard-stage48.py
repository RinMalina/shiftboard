# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: ShiftBoard
import unittest
from shiftboard.models import Shift, Role, StaffMember, Availability, Swap
from datetime import date


class TestShiftCreation(unittest.TestCase):
    def test_create_shift(self):
        s = Shift(
            id=1,
            role=Role(name="Nurse"),
            start=date(2024, 1, 15),
            end=date(2024, 1, 16),
            staff=[StaffMember(id=1)],
        )
        self.assertEqual(s.id, 1)
        self.assertEqual(len(s.staff), 1)

    def test_create_availability(self):
        a = Availability(start=date(2024, 1, 15), end=date(2024, 1, 16))
        self.assertTrue(a.start < a.end)


class TestSwapValidation(unittest.TestCase):
    def test_invalid_swap_dates(self):
        with self.assertRaises(ValueError):
            Swap(start=date(2024, 1, 16), end=date(2024, 1, 15))

    def test_valid_swap(self):
        s = Swap(start=date(2024, 1, 15), end=date(2024, 1, 16))
        self.assertEqual(s.start, date(2024, 1, 15))


if __name__ == "__main__":
    unittest.main()
