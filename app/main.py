from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from database import get_db
from sqlalchemy.orm import Session
import crud

app = FastAPI(
    docs=False,
    title="Fastapi with database!"
)

app.get("/", response_class=HTMLResponse)
def get_main_page():
    return """
    <html>
    <head>
    </head>
    <body>
        <h1> Hello World!! </h1>
        <p> For create a note create a url address with query params: value(int) and description(string). Path: /add. Example: http://<host>/add?value=1&description="Nice work"</p>
        <p> For see all notes with the same value go to http://<host>/get&value=<your value> </p>
    </body>
    </html>
    """

@app.get("/get", response_model=HTMLResponse)
def get_notes(value: int, db: Session = Depends(get_db)):
    notes = crud.get_note(value=value, db=db)
    if type(notes) == list:
        all_notes_str = ''.join(notes)
        return f"""
        <html>
        <head>
        </head>
        <body>
            <h1> Hello World!! </h1>
            <p> Thats all: {all_notes_str}
        </body>
        </html>
        """
    else:
        return """
        <html>
        <head>
        </head>
        <body>
            <h1> NOT FOUND </h1>
        </body>
        </html>
        """

@app.post("/add")
def add_note(description: str,value: int, db: Session = Depends(get_db)):
    is_allow = crud.add_note(db=db, value=value, des=description)
    return {"added" : is_allow}