# === Stage 19: Add undo support for the last simple mutation ===
# Project: ShiftBoard
def undo(self):
        if self._undo_stack:
            action, state = self._undo_stack.pop()
            for key in list(state.keys()):
                del state[key]
            if isinstance(action, tuple) and len(action) == 2:
                role, shift = action
                shifts[role].append(shift)
                return True
