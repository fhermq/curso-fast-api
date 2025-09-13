from typing import Annotated
from pydantic import AfterValidator, BaseModel, field_validator

# After: se ejecuta despues de validaciones/transformaciones de pydantic
# Before: se ejecuta antes de validaciones/transformaciones de pydantic
# Plain: similar a before, termina la validacion al retornar el valor.
# Wrap: Flexible para ejecutarse antes o despues de las validaciones de pydantic.

## ==========  ANNOTATED =========== ##
def is_odd (value: int) -> int:
    if value % 2 == 1:
        raise ValueError(f"{value} no es un numero par")
    return value
    
NumeroPar = Annotated[int, AfterValidator(is_odd)]

class Model1(BaseModel):
    # NumeroPar = Annotated[int, AfterValidator(is_odd)]
    my_number: NumeroPar

#ejemplo: Model1 = Model1(my_number=4)


class Model2(BaseModel):
    other_number: Annotated[NumeroPar, AfterValidator(lambda v : v + 2 )]

#ejemplo2: Model2 = Model2(other_number=0)
#print(ejemplo2)

class Model3(BaseModel):
    lista_pares: list[NumeroPar]
#ejemplo3: Model3 = Model3(lista_pares=[-100,6,10])
#print(ejemplo3)


# =========== Usando DECORATOR ===============#

class Item(BaseModel):
    item_id: int
    price: float

    @field_validator("item_id", "price", mode="after")
    def check_positive(cls,value:int | float):
        if value < 0:
            raise ValueError("Item debe ser positivo")
        return value
    
banana = Item = Item(item_id=2, price=2.7)
