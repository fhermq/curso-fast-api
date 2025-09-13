#Pydantic
#After
#Before
#Wrap

from typing_extensions import Self
from pydantic import BaseModel, model_validator

class UserModel(BaseModel):
    username: str
    password: str
    password_repeat: str

    @model_validator(mode="after")
    def check_passwords(self) -> Self:
        if self.password != self.password_repeat:
            raise ValueError("Objeto incorrecto, passwords no coinciden")
        return self
    
usuario1: UserModel = UserModel(username="Fernando", password="1234", password_repeat="1234")
