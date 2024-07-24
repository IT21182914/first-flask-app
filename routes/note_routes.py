from flask import Blueprint, request, jsonify
from controllers.note_controller import (
    get_all_notes,
    get_note_by_id,
    create_note,
    update_note,
    delete_note
)

note_bp = Blueprint('note_bp', __name__)

@note_bp.route('/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    create_note(data['title'], data['content'])
    return jsonify({'message': 'Note created'})

@note_bp.route('/notes', methods=['GET'])
def get_notes():
    notes = get_all_notes()
    return jsonify([{'id': note.id, 'title': note.title, 'content': note.content} for note in notes])

@note_bp.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = get_note_by_id(note_id)
    if note:
        return jsonify({'id': note.id, 'title': note.title, 'content': note.content})
    return jsonify({'message': 'Note not found'}), 404

@note_bp.route('/notes/<int:note_id>', methods=['PUT'])
def update_note_route(note_id):
    data = request.get_json()
    update_note(note_id, data['title'], data['content'])
    return jsonify({'message': 'Note updated'})

@note_bp.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note_route(note_id):
    delete_note(note_id)
    return jsonify({'message': 'Note deleted'})
