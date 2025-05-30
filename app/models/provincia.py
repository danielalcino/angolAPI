from pydantic import BaseModel

class Provincia(BaseModel):
    nome: str
    capital: str

