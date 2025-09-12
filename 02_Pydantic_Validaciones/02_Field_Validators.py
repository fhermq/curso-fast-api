from typing import Annotated
from pydantic import AfterValidator, BaseModel

# After: se ejecuta despues de validaciones/transformaciones de pydantic
# Before: se ejecuta antes de validaciones/transformaciones de pydantic
# Plain: similar a before, termina la validacion al retornar el valor.
# Wrap: Flexible para ejecutarse antes o despues de las validaciones de pydantic.


def is_odd (value: int) -> int:
    if value % 2 == 1:
        raise ValueError(f"{value} no es un numero par")
    
NumeroPar = Annotated[int, AfterValidator(is_odd)]

class Model1(BaseModel):
    # NumeroPar = Annotated[int, AfterValidator(is_odd)]
    my_number: NumeroPar

ejemplo: Model1 = Model1(my_number=3)

