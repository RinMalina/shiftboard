# === Stage 51: Add unit tests for search and filter behavior ===
# Project: ShiftBoard
import unittest
from shiftboard.models import Shift, Role, StaffMember
from shiftboard.repository import shift_repository

class TestSearchAndFilter(unittest.TestCase):
    def setUp(self):
        self.repo = shift_repository()
        self.repo.add_shift(Shift(id=1, role=Role(id=1, name="Nurse"), staff=StaffMember(id=1, name="Alice"), start="08:00", end="16:00"))
        self.repo.add_shift(Shift(id=2, role=Role(id=1, name="Nurse"), staff=StaffMember(id=2, name="Bob"), start="09:00", end="17:00"))
        self.repo.add_shift(Shift(id=3, role=Role(id=2, name="Doctor"), staff=StaffMember(id=1, name="Alice"), start="10:00", end="18:00"))

    def test_search_by_staff(self):
        results = self.repo.search_shifts_by_staff("Alice")
        self.assertEqual(len(results), 2)
        ids = {s.id for s in results}
        self.assertIn(1, ids)
        self.assertIn(3, ids)

    def test_search_by_role(self):
        results = self.repo.search_shifts_by_role("Nurse")
        self.assertEqual(len(results), 2)
        ids = {s.id for s in results}
        self.assertIn(1, ids)
        self.assertIn(2, ids)

    def test_search_by_date_range(self):
        results = self.repo.search_shifts_by_date_range("08:00", "17:00")
        self.assertEqual(len(results), 3)

    def test_search_by_staff_and_date(self):
        results = self.repo.search_shifts_by_staff_and_date("Alice", "08:00", "18:00")
        self.assertEqual(len(results), 2)

    def test_search_by_role_and_date(self):
        results = self.repo.search_shifts_by_role_and_date("Nurse", "08:00", "17:00")
        self.assertEqual(len(results), 2)

    def test_search_by_staff_role_and_date(self):
        results = self.repo.search_shifts_by_staff_role_and_date("Alice", "Nurse", "08:00", "18:00")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, 1)

if __name__ == "__main__":
    unittest.main()
