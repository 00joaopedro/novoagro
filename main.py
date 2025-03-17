from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, FileSystemLoader  # 🔹 Importação corrigida
from fastapi import FastAPI
from api import router as api_router, link_pagamento  # Importa API e função de pagamento

# Inclui as rotas no app principal
app = FastAPI()

# Configuração do Jinja2 para templates
env = Environment(loader=FileSystemLoader("templates"))

# Incluindo as rotas da API

@app.get("/", response_class=HTMLResponse)
async def siteagro(request: Request):
    link_iniciar_pagamento = link_pagamento()  # 🔹 Agora funciona corretamente
    template = env.get_template("index.html")
    return template.render(link_pagamento=link_iniciar_pagamento)

@app.get("/errado", response_class=HTMLResponse)
async def errado(request: Request):
    template = env.get_template("errado.html")
    return template.render()

@app.get("/certo", response_class=HTMLResponse)
async def certo(request: Request):
    template = env.get_template("certo.html")
    return template.render()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
