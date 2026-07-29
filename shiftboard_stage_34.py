# === Stage 34: Add support for multiple local user profiles ===
# Project: ShiftBoard
import json, os


PROFILES_DIR = "profiles"


def load_profiles():
    if not os.path.isdir(PROFILES_DIR):
        return {}
    profiles = {}
    for fname in sorted(os.listdir(PROFILES_DIR)):
        if not fname.endswith(".json"):
            continue
        path = os.path.join(PROFILES_DIR, fname)
        with open(path) as f:
            data = json.load(f)
        name = data.get("name", fname.replace(".json", "").replace("_", " "))
        profiles[name] = {**data, "_path": path}
    return profiles


def save_profile(name, profile):
    os.makedirs(PROFILES_DIR, exist_ok=True)
    path = os.path.join(PROFILES_DIR, f"{name.lower().strip().replace(' ', '_')}.json")
    with open(path, "w") as f:
        json.dump(profile, f, indent=2)


def add_profile(name, **kwargs):
    if name in load_profiles():
        raise ValueError(f"Profile {name!r} already exists.")
    profile = {"name": name, **kwargs}
    save_profile(name, profile)
    return profile


def remove_profile(name):
    path = os.path.join(PROFILES_DIR, f"{name.lower().strip().replace(' ', '_')}.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Profile {name!r} not found.")
    os.remove(path)
