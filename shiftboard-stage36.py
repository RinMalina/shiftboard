# === Stage 36: Add templates for quickly creating common records ===
# Project: ShiftBoard
class ShiftTemplates:
    """Quickly create common shift and roster records."""
    
    @staticmethod
    def standard_shift(role_name, start_time, end_time):
        return {
            'role': role_name,
            'start': start_time,
            'end': end_time,
            'status': 'pending'
        }
    
    @staticmethod
    def swap_request(shift_id, reason):
        return {'shift_id': shift_id, 'reason': reason, 'approved': False}
    
    @staticmethod
    def weekly_roster(template_shifts=None):
        if template_shifts is None:
            template_shifts = [
                ShiftTemplates.standard_shift('Morning', '08:00', '12:00'),
                ShiftTemplates.standard_shift('Afternoon', '13:00', '17:00')
            ]
        return {'week': 'current', 'shifts': template_shifts, 'coverage_ok': True}
