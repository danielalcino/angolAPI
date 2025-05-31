from fastapi import APIRouter
from app.models.provincia import Provincia

router = APIRouter(
    prefix="/provincias",
    tags=["Provincias"]
)

@router.get("/", response_model=list[Provincia])
def listar_provincias():
    return [
        {"nome": "Bengo", "capital": "Caxito"},
        {"nome": "Benguela", "capital": "Benguela"},
        {"nome": "Bié", "capital": "Kuito"},
        {"nome": "Cabinda", "capital": "Cabinda"},
        {"nome": "Cuando Cubango", "capital": "Menongue"},
        {"nome": "Cuanza Norte", "capital": "Ndalatando"},
        {"nome": "Cuanza Sul", "capital": "Sumbe"},
        {"nome": "Cunene", "capital": "Ondjiva"},
        {"nome": "Huambo", "capital": "Huambo"},
        {"nome": "Huíla", "capital": "Lubango"},
        {"nome": "Luanda", "capital": "Luanda"},
        {"nome": "Lunda Norte", "capital": "Dundo"},
        {"nome": "Lunda Sul", "capital": "Saurimo"},
        {"nome": "Malanje", "capital": "Malanje"},
        {"nome": "Moxico", "capital": "Luena"},
        {"nome": "Namibe", "capital": "Moçâmedes"},
        {"nome": "Uíge", "capital": "Uíge"},
        {"nome": "Zaire", "capital": "M'banza Kongo"},
        {"nome": "Cassongue", "capital": "Cassongue"},
        {"nome": "Cacuso", "capital": "Cacuso"},
        {"nome": "Luena Norte", "capital": "Lucusse"},
        {"nome": "Lumbala Nguimbo", "capital": "Lumbala Nguimbo"},
        {"nome": "Luengue", "capital": "Luengue"}
    ]

