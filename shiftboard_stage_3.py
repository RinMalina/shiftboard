# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: ShiftBoard
def validate_required(value, field_name):
    if value is None or (isinstance(value, str) and value.strip() == ''):
        raise ValueError(f"{field_name} must not be empty")
    return value


def validate_identifier(value):
    if not isinstance(value, str) or len(value.strip()) < 3:
        raise ValueError("Identifier must be a string of at least 3 characters")
    cleaned = value.strip()
    return cleaned.lower().replace(' ', '_')


def validate_short_text(value, max_length=50):
    if not isinstance(value, str) or len(value.strip()) == 0:
        raise ValueError("Short text must be a non-empty string")
    if len(value.strip()) > max_length:
        raise ValueError(f"Short text exceeds {max_length} characters")
    return value.strip()[:max_length]
