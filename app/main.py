from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import provincias

app = FastAPI(
    title="AngolAPI",
    description="API pública com dados estruturados de Angola.",
    version="0.1.0"
)

# Permitir acesso externo (por exemplo, frontend em React ou Flutter)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, defina os domínios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas
app.include_router(provincias.router)

