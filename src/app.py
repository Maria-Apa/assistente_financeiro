# ============= IMPORTS =============
import json
import streamlit as st
from openai import OpenAI
import re

# ============= CONFIGURAÇÃO =============
client = OpenAI(api_key="SUA_CHAVE"  # você pode trocar para gpt-4.1-nano para pagar menos

# ============= CARREGAR DADOS =============
produtos = json.load(open('./data/produtos_financeiros.json', encoding='utf-8'))
info_financeira = json.load(open('./data/info_financeira.json', encoding='utf-8'))
riscos_financeiros = json.load(open('./data/riscos_financeiros.json', encoding='utf-8'))
tributacao_financeira = json.load(open('./data/tributacao_financeira.json', encoding='utf-8'))
perfil_investidor = json.load(open('./data/perfil_investidor.json', encoding='utf-8'))

# ============= SYSTEM PROMPT =============
SYSTEM_PROMPT = """
Você é Lumi, um assistente financeiro projetado para ajudar as pessoas a entender por onde começar seus investimentos de acordo com o perfil de cada uma.

Como você deve atuar:

Primeiro, procure entender os objetivos do usuário e o perfil de investidor. Utilize as informações armazenadas nos arquivos JSON para apresentar categorias de produtos que podem se encaixar no que a pessoa busca. Sempre explique cada conceito de forma simples, como se estivesse conversando com um amigo.

REGRAS:
- Você nunca recomendará um investimento específico, apenas apresentará categorias, possibilidades e como funcionam.
- Você sempre baseará suas respostas exclusivamente nos dados da base de conhecimento fornecida (JSONs).
- Se a informação não estiver explicitamente presente em nenhum JSON, responda apenas: ‘Não tenho essa informação na minha base.’
- Não explique nada adicional sobre investimentos, não complemente e não ofereça contexto externo.
- Quando uma informação não estiver presente na base, diga: 'Não tenho essa informação na minha base, gostaria de verificar as informações de outro produto?'
- Não invente números, taxas, datas, prazos ou rentabilidades.
- Se o usuário pedir cálculos, responda: 'Não faço simulações...'
- Nunca finja ter acesso a dados bancários, extratos, saldos ou sistemas externos.
- Utilize linguagem simples e didática.
- Sempre pergunte ao final se o usuário entendeu ou se ficou alguma dúvida.
"""

# ============= MONTAR CONTEXTO =============
def montar_contexto(msg):
    contexto = []
    msg_lower = msg.lower()

    if any(p in msg_lower for p in ["perfil", "conservador", "moderado", "arrojado"]):
        contexto.append("PERFIL DO INVESTIDOR:\n" + json.dumps(perfil_investidor, indent=2, ensure_ascii=False))

    if any(p in msg_lower for p in ["invest", "cdb", "tesouro", "fundo", "lci", "lca"]):
        contexto.append("PRODUTOS FINANCEIROS:\n" + json.dumps(produtos, indent=2, ensure_ascii=False))

    if "risco" in msg_lower:
        contexto.append("RISCOS FINANCEIROS:\n" + json.dumps(riscos_financeiros, indent=2, ensure_ascii=False))

    if any(t in msg_lower for t in ["imposto", "ir", "tribut"]):
        contexto.append("TRIBUTAÇÃO:\n" + json.dumps(tributacao_financeira, indent=2, ensure_ascii=False))

    if any(x in msg_lower for x in ["o que é", "como funciona", "explica", "defina"]):
        contexto.append("INFORMAÇÕES FINANCEIRAS:\n" + json.dumps(info_financeira, indent=2, ensure_ascii=False))

    return "\n\n".join(contexto)

# ============= FUNÇÃO PRINCIPAL =============
def perguntar(msg):
    contexto_dinamico = montar_contexto(msg)

    response = client.responses.create(
        model=MODELO,
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"{contexto_dinamico}\n\nPergunta: {msg}"}
        ]
    )

    return response.output_text

# ============= INTERFACE =============
st.title("Lumi — Seu Assistente Financeiro Educação 😊")

if pergunta := st.chat_input("Pergunte algo sobre finanças:"):
    st.chat_message("user").write(pergunta)

    with st.spinner("Lumi está pensando..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
