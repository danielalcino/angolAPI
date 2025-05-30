# 🇦🇴 AngolAPI

**AngolAPI** é uma API pública e gratuita que fornece dados estruturados sobre Angola, como províncias, municípios, feriados, documentos oficiais, serviços e muito mais.

Inspirado no [BrasilAPI](https://brasilapi.com.br/), este projeto visa facilitar o acesso a dados nacionais de forma simples, padronizada e segura — ideal para uso por desenvolvedores, pesquisadores, empresas e órgãos públicos.

---

## 🚀 Objetivos

- Centralizar informações públicas sobre Angola.
- Fornecer acesso gratuito a dados via HTTP.
- Promover transparência e inovação tecnológica no país.
- Estimular o desenvolvimento de soluções digitais baseadas em dados nacionais.

---

## 📚 Endpoints disponíveis (em desenvolvimento)

| Recurso     | Endpoint                | Status     |
|-------------|-------------------------|------------|
| Províncias  | `/provincias`           | ✅ Pronto  |
| Municípios  | `/municipios`           | 🚧 Em breve |
| Feriados    | `/feriados`             | 🧪 Planejado |
| Documentos  | `/documentos`           | 🧪 Planejado |
| Saúde       | `/postos-saude`         | 🧪 Planejado |

---

## 🧰 Tecnologias usadas

- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://docs.pydantic.dev/)

---

## 🛠️ Como executar localmente

```bash
git clone https://github.com/seu-usuario/angolapi.git
cd angolapi
pip install -r requirements.txt
uvicorn app.main:app --reload
