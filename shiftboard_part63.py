# === Stage 63: Add relationships between records where useful ===
# Project: ShiftBoard
class ShiftBoardRelationships:
    """Establish relationships between ShiftBoard records for richer queries."""

    def __init__(self, db, staff_model, shift_model, role_model, availability_model):
        self.db = db
        self.staff_model = staff_model
        self.shift_model = shift_model
        self.role_model = role_model
        self.availability_model = availability_model

    def associate_staff_with_shifts(self):
        for staff in self.db.query(self.staff_model).all():
            staff.shifts = self.db.query(self.shift_model).filter_by(staff_id=staff.id).all()

    def associate_staff_with_roles(self):
        for staff in self.db.query(self.staff_model).all():
            staff.roles = self.db.query(self.role_model).filter_by(staff_id=staff.id).all()

    def associate_shift_with_roles(self):
        for shift in self.db.query(self.shift_model).all():
            shift.roles = self.db.query(self.role_model).filter_by(shift_id=shift.id).all()

    def associate_staff_with_availability(self):
        for staff in self.db.query(self.staff_model).all():
            staff.availability = self.db.query(self.availability_model).filter_by(staff_id=staff.id).all()

    def associate_shifts_with_availability(self):
        for shift in self.db.query(self.shift_model).all():
            shift.availability = self.db.query(self.availability_model).filter_by(shift_date=shift.start_date).all()
