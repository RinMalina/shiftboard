# === Stage 28: Add overdue item detection based on due dates ===
# Project: ShiftBoard
def detect_overdue_items(tasks, due_date):
    """Detect tasks that are past their due date."""
    overdue = []
    for task in tasks:
        if hasattr(task, 'due_date') and task['due_date'] < due_date:
            overdue.append({
                'id': task['id'],
                'title': task.get('title', 'Unknown'),
                'overdue_by': (due_date - task['due_date']).days
            })
    return overdue

# Example usage with sample data
sample_tasks = [
    {'id': 1, 'title': 'Project Alpha', 'due_date': '2024-01-15'},
    {'id': 2, 'title': 'Report Beta', 'due_date': '2024-03-20'},
    {'id': 3, 'title': 'Design Gamma', 'due_date': '2024-06-10'}
]

# Check for overdue items relative to today (or any reference date)
today = datetime.date.today()
overdue_items = detect_overdue_items(sample_tasks, today)

if overdue_items:
    print(f"Found {len(overdue_items)} overdue item(s):")
    for item in overdue_items:
        print(f"- {item['title']}: overdue by {item['overdue_by']} days")
else:
    print("No overdue items found!")
