from fastapi import FastAPI, HTTPException
from pydantic import BaseModel




app=FastAPI()

Books = [
    {"id":1,"title":"Book 1","author":"Author 1"},
    {"id":2,"title":"Book 2","author":"Author 2"},
]


@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/books")
def book():
    return Books

@app.get("/book/{id}")
def get_book(id: int):
    for book in Books:
        if book["id"] == id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

class Book(BaseModel):
    id: int
    title: str
    author: str
    
@app.post("/book")
def add_book(book: Book):
    Books.append(book.dict())
    return book


class UpdateBook(BaseModel):
    title: str
    author: str
    
@app.put("/book/{id}")
def update_book(id: int, book: UpdateBook):
    for b in Books:
        if b["id"] == id:
            b["title"] = book.title
            b["author"] = book.author
            return b
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/book/{id}")
def delete_book(id: int):
    for b in Books:
        if b["id"] == id:
            Books.remove(b)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")


