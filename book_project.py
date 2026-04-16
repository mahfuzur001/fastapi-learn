from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from database import get_db,engine
from model import Book
from sqlalchemy.orm import Session


app=FastAPI()

@app.get("/")
def home():
    return {"message": "this is home page"}

@app.get("/books")
def book(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books

@app.get("/book/{id}")
def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book




class BookCreate(BaseModel):
    id: int
    title: str
    author: str
    
@app.post("/book")
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(id=book.id, title=book.title, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

class UpdateBook(BaseModel):
    title: str
    author: str
    

@app.put("/book/{id}")
def update_book(id: int, book: UpdateBook, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db_book.title = book.title
    db_book.author = book.author
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/book/{id}")
def delete_book(id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted"}