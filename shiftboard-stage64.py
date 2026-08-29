# === Stage 64: Add validation for relationship references ===
# Project: ShiftBoard
def validate_relationship_refs(relationships):
    """Validate that all referenced entities exist in the roster."""
    errors = []
    for rel in relationships:
        if rel.source not in roster['employees']:
            errors.append(f"Employee '{rel.source}' not found in roster.")
        if rel.target not in roster['employees']:
            errors.append(f"Employee '{rel.target}' not found in roster.")
        if rel.role not in roster['roles']:
            errors.append(f"Role '{rel.role}' not found in roster.")
        if rel.shift not in roster['shifts']:
            errors.append(f"Shift '{rel.shift}' not found in roster.")
    return errors
