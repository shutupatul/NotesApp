def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["note"]["title"],
        "desc": item["note"]["desc"],
        "important": item["note"]["important"]
    }

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]