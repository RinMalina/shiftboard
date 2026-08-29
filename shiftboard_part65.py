# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: ShiftBoard
def merge_imports(existing_imports: dict, new_imports: dict) -> dict:
    merged = {}
    for module, alias in new_imports.items():
        if module not in existing_imports:
            merged[module] = alias
        else:
            existing_alias = existing_imports[module]
            if alias != existing_alias:
                raise ValueError(
                    f"Duplicate import for {module!r}: "
                    f"existing alias {existing_alias!r} vs new alias {alias!r}"
                )
    return merged
