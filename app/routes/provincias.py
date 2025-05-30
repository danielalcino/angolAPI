from fastapi import APIRouter
from app.models.provincia import Provincia

router = APIRouter(
    prefix="/provincias",
    tags=["Provincias"]
)

@router.get("/", response_model=list[Provincia])
def listar_provincias():
    return [
        {"nome": "Luanda", "capital": "Luanda"},
        {"nome": "Benguela", "capital": "Benguela"},
        {"nome": "Huambo", "capital": "Huambo"},
    ]

