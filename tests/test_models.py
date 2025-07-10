
from app.models import Note

def test_note_value_range():
    note = Note(value=15)
    assert 0 <= note.value <= 20

def test_average_calculation():
    notes = [Note(value=15), Note(value=17), Note(value=18)]
    average = sum(n.value for n in notes) / len(notes)
    assert average == 16.666666666666668
