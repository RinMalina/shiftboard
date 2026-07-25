# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: ShiftBoard
def tag_add(tag_name, tag_list):
    if tag_name in tag_list:
        return tag_list
    tag_list.append(tag_name)
    return tag_list

def tag_remove(tag_name, tag_list):
    if tag_name not in tag_list:
        return tag_list
    tag_list.remove(tag_name)
    return tag_list

def summarize_tags(tags, max_len=30):
    if len(tags) == 0:
        return "(none)"
    short = ", ".join(tags[:max_len // 15])
    if len(tags) > max_len // 15:
        short += ", ..."
    return f"[{short}]"

def tag_stats(tag_list):
    counts = {}
    for t in tag_list:
        counts[t] = counts.get(t, 0) + 1
    return dict(sorted(counts.items(), key=lambda x: -x[1]))
