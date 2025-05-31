from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.routes import provincias
import os
from app.services.geonames_service import buscar_provincias_geonames

app = FastAPI(
    title="AngolAPI",
    description="API pública com dados estruturados de Angola.",
    version="0.1.0"
)

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "../templates"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(provincias.router)

@app.get("/sync/provincias", response_class=HTMLResponse)
def sync_provincias(request: Request):
    username = "danielkapwata"
    provincias = buscar_provincias_geonames(username)
    print(provincias)  # Debug: ver o que é retornado
    return templates.TemplateResponse("provincias.html", {"request": request, "provincias": provincias})

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

