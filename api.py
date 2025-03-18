from fastapi import APIRouter
import mercadopago  

router = APIRouter()

@router.get("/")
async def teste():
    return {"mensagem": "Rota funcionando!"}

# Função de pagamento importável para o main.py
def link_pagamento():
    sdk = mercadopago.SDK("APP_USR-1588218199296186-030923-f8d6e6b51ed1eed28a231f9b16d089bc-1456006594")
    payment_data = {
        "items": [
            {"id": "venda", "title": "vaga", "quantity": 1, "currency_id": "BRL", "unit_price": 100.00},
            {"id": "venda2", "title": "vaga", "quantity": 1, "currency_id": "BRL", "unit_price": 200.00}
        ],
        "back_urls": {
            "success": "http://127.0.0.1:8000/certo",
            "failure": "http://127.0.0.1:8000/errado",
            "pending": "http://127.0.0.1:8000/errado"
        },
        "auto_return": "all"
    }

    result = sdk.preference().create(payment_data)
    payment = result.get("response", {})
    link_iniciar_pagamento = payment.get("init_point", None)

    if not link_iniciar_pagamento:
        print("⚠️ Erro ao gerar link de pagamento:", result)

    return link_iniciar_pagamento
