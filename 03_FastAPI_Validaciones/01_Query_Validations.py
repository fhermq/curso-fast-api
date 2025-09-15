from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import AfterValidator

app = FastAPI()
# Strings
# max_length
# min_length
# pattern

# Numbers
# gt 
# ge
# lt
# le

def check_valid_number(id: str):
    if id % 2 != 0:
        raise ValueError("Debe ser un número par")
    return id


@app.get("/items/")
async def read_items(q: Annotated[ int | None , Query(lt=10, ge=5)] = None):
#async def read_items(q: Annotated[ int | None , AfterValidator(check_valid_number)] = None):
    results: dict = {"mensaje": "Acceso a get(read_items)"}
    if q:
        results.update({"q": q})
    return results
