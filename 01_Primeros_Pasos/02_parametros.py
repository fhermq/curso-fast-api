from fastapi import FastAPI

app = FastAPI()

#Rutas fijas deben ir primero, en caso de ser la misma toma la primera que encuentra.
@app.get("/books/favorite")
async def get_favorite_book():
    return {"title": "1984 - Orwell"}

@app.get("/books/{book_id}")
async def get_book(book_id:int):
    return {"book_id": book_id }