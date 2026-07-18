# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: ShiftBoard
def update_record(self, record_id, field_name, new_value):
    if record_id is None:
        raise ValueError("record_id must be provided for updates")
    table = self._tables.get(record_id)
    if table is None or record_id not in table.records:
        raise KeyError(f"No {record_id} record found to update")
    if field_name == "id":
        raise ValueError("Cannot modify the 'id' field")
    old_value = table.records[record_id].get(field_name)
    new_record = dict(table.records[record_id])
    new_record[field_name] = new_value
    table.records[record_id] = new_record
