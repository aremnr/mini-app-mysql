from sqlalchemy.orm import Session
import app.models as models


def get_note(db: Session, value: int) -> list | bool:
    try:
        notes = db.query(models.MyTestTable).filter(models.MyTestTable.value == value).all()
        print(notes)
        assert len(notes) != 0
        notes_description = [i.description for i in notes]
        return notes_description
    except:
        return False

def add_note(db: Session, value: int, des: str) -> bool:
    new_note = models.MyTestTable(value=value, description=des)
    db.add(new_note)
    db.commit()
    return True