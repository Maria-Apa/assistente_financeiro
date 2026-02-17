from groq import Groq
from core.regras import SYSTEM_PROMPT
from core.contexto import montar_contexto
from core.calculadora import verificar_calculo

client = Groq(api_key="sua_chave")
MODELO = "llama-3.1-8b-instant"

def perguntar(msg):
    negado = verificar_calculo(msg)
    if negado:
        return negado

    contexto = montar_contexto(msg)

    response = client.chat.completions.create(
        model=MODELO,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"{contexto}\n\nPergunta: {msg}"}
        ]
    )

    return response.choices[0].message.content
