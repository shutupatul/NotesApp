from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from models.note import Note
from fastapi.templating import Jinja2Templates
from config.db import conn
from pathlib import Path
from schemas.note import noteEntity, notesEntity

note = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).resolve().parent.parent / "templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),
            "title": doc["note"]["title"],  # Check if this exists
            "desc": doc["note"]["desc"],    # Check if this exists
            "important": doc["note"]["important"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


@note.post("/")
async def create_item(request: Request):
    form = await request.json()

    title = form.get("title")
    desc = form.get("desc")
    important = form.get("important", False)

    print("Received data:", form)

    note_document = {
        "note": {
            "title": title,
            "desc": desc,
            "important": important
        }
    }

    result = conn.notes.notes.insert_one(note_document)

    print("Inserted document ID:", result.inserted_id)

    return {"Success": True, "inserted_id": str(result.inserted_id)}
