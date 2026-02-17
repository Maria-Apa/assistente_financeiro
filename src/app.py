# ============= IMPORTS =============
import json
import streamlit as st
from groq import Groq
import re

# ============= CONFIGURAÇÃO =============
client = Groq(api_key="sua_chave")
MODELO = "llama-3.1-8b-instant"

# ============= CARREGAR DADOS =============
produtos = json.load(open('./data/produtos_financeiros.json', encoding='utf-8'))
info_financeira = json.load(open('./data/info_financeira.json', encoding='utf-8'))
riscos_financeiros = json.load(open('./data/riscos_financeiros.json', encoding='utf-8'))
tributacao_financeira = json.load(open('./data/tributacao_financeira.json', encoding='utf-8'))
perfil_investidor = json.load(open('./data/perfil_investidor.json', encoding='utf-8'))

# ============= COMO O AGENTE LIDA COM PEDIDOS DE CÁLCULO =============
def verificar_calculo(msg):
    if any(palavra in msg.lower() for palavra in ["calcule", "simule", "quanto rende", "%", "juros"]):
        return "Não faço simulações ou cálculos, mas posso te explicar como o conceito funciona 😊"
    return None

# ============= SYSTEM PROMPT =============
SYSTEM_PROMPT = """
Você é Lumi, um assistente financeiro projetado para ajudar as pessoas a entender por onde começar seus investimentos de acordo com o perfil de cada uma.

Como você deve atuar

Primeiro, procure entender os objetivos do usuário e o perfil de investidor. Utilize as informações armazenadas nos arquivos JSON para apresentar categorias de produtos que podem se encaixar no que a pessoa busca. Sempre explique cada conceito de forma simples, como se estivesse conversando com um amigo.

REGRAS:
- Você nunca recomendará um investimento específico, apenas apresentará categorias, possibilidades e como funcionam.
- Você sempre baseará suas respostas exclusivamente nos dados da base de conhecimento fornecida (JSONs).
- Quando uma informação não estiver presente na base, diga:
'Não tenho essa informação na minha base, mas posso explicar o conceito de forma geral.'
- Não invente números, taxas, datas, prazos ou rentabilidades.
- Se o usuário pedir cálculos, responda:
'Não faço simulações, mas posso te explicar como o cálculo funciona.'
- Nunca finja ter acesso a dados bancários, extratos, saldos ou sistemas externos.
- Utilize linguagem simples e didática.
- Sempre pergunte ao final se o usuário entendeu ou se ficou alguma dúvida.
"""

# ============= MONTAR CONTEXTO =============
def montar_contexto(msg):
    contexto = []
    msg_lower = msg.lower()

    # Perfil do investidor
    if any(p in msg_lower for p in ["perfil", "conservador", "moderado", "arrojado"]):
        contexto.append("PERFIL DO INVESTIDOR:\n" + json.dumps(perfil_investidor, indent=2, ensure_ascii=False))

    # Produtos financeiros
    if any(p in msg_lower for p in ["invest", "cdb", "tesouro", "fundo", "lci", "lca"]):
        contexto.append("PRODUTOS FINANCEIROS:\n" + json.dumps(produtos, indent=2, ensure_ascii=False))

    # Riscos
    if "risco" in msg_lower:
        contexto.append("RISCOS FINANCEIROS:\n" + json.dumps(riscos_financeiros, indent=2, ensure_ascii=False))

    # Tributação
    if "imposto" in msg_lower or "ir" in msg_lower or "tribut" in msg_lower:
        contexto.append("TRIBUTAÇÃO:\n" + json.dumps(tributacao_financeira, indent=2, ensure_ascii=False))

    # Conceitos gerais
    if any(x in msg_lower for x in ["o que é", "como funciona", "explica", "defina"]):
        contexto.append("INFORMAÇÕES FINANCEIRAS:\n" + json.dumps(info_financeira, indent=2, ensure_ascii=False))

    return "\n\n".join(contexto)

# ============= FUNÇÃO PRINCIPAL ============
def perguntar(msg):
    negado = verificar_calculo(msg)
    if negado:
        return negado

    contexto_dinamico = montar_contexto(msg)

    response = client.chat.completions.create(
        model=MODELO,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"{contexto_dinamico}\n\nPergunta: {msg}"}
        ]
    )
    return response.choices[0].message.content

# ============= INTERFACE =============
st.title("Lumi — Seu Assistente Financeiro Educação 😊")

if pergunta := st.chat_input("Pergunte algo sobre finanças:"):
    st.chat_message("user").write(pergunta)

    with st.spinner("Lumi está pensando..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
