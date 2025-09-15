from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(
    item_id: Annotated[int,Path(ge=10, title="ID de Item")], 
    q: Annotated[str|None, Query(alias="item_query")]= None):
    results: dict = {"mensaje": "Acceso a get(item)"}
    if item_id:
        results.update({"id": item_id})
    return results
