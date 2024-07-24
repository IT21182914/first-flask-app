from models.note_model import Note
from app import db

def get_all_notes():
    return Note.query.all()

def get_note_by_id(note_id):
    return Note.query.get(note_id)

def create_note(title, content):
    new_note = Note(title=title, content=content)
    db.session.add(new_note)
    db.session.commit()

def update_note(note_id, title, content):
    note = Note.query.get(note_id)
    if note:
        note.title = title
        note.content = content
        db.session.commit()

def delete_note(note_id):
    note = Note.query.get(note_id)
    if note:
        db.session.delete(note)
        db.session.commit()
