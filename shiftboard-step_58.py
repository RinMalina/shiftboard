# === Stage 58: Add bulk update behavior for selected records ===
# Project: ShiftBoard
# Step 58: Bulk update selected records.
# Append to existing ShiftBoard.py.

def bulk_update_records(db, records, fields):
    """Update multiple records in bulk.

    Args:
        db: SQLAlchemy database instance.
        records: List of dicts with 'id' and field values to update.
        fields: List of field names to update in all records.

    Returns:
        Number of successfully updated records.
    """
    if not records or not fields:
        return 0

    session = db.session()
    try:
        for record in records:
            if 'id' not in record:
                continue
            obj = session.query(Record).get(record['id'])
            if obj is None:
                continue
            for field in fields:
                if field in record:
                    setattr(obj, field, record[field])
        session.commit()
        return len(records)
    except Exception as e:
        session.rollback()
        print(f"Error updating records: {e}")
        return 0
    finally:
        session.close()
