# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: ShiftBoard
class Scorer:
    """Simple scoring for shift recommendations based on staff preferences and history."""

    def __init__(self, history=None):
        self.history = history or {}

    def set_history(self, history):
        self.history = history

    def get_history(self):
        return self.history

    def score_shift(self, staff_id, shift, available_shifts, history=None):
        if history is None:
            history = self.history
        score = 0
        if staff_id in history and shift in history[staff_id]:
            score -= history[staff_id][shift] * 10
        return score

    def get_best_shift(self, staff_id, available_shifts, history=None):
        if history is None:
            history = self.history
        best_shift = None
        best_score = float('-inf')
        for shift in available_shifts:
            score = self.score_shift(staff_id, shift, available_shifts, history)
            if score > best_score:
                best_score = score
                best_shift = shift
        return best_shift
