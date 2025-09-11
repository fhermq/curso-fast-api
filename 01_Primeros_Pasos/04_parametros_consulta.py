from fastapi import FastAPI

app = FastAPI()

cars_list: list[dict] = [
    {"car_name": "Elantra"},
    {"car_name": "Civic"},
    {"car_name": "Sentra"},
    {"car_name": "Corola"}
]

@app.get("/cars/")
async def get_cars(skip:int, limit: int, opt:str | None = None):
    if opt:
        return{
            "list:": cars_list[skip:skip + limit],
            "optional": opt
        }
    return cars_list[skip: skip+limit]