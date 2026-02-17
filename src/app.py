import streamlit as st
from core.agente import perguntar

st.title("Lumi — Seu Assistente Financeiro Educação 😊")

pergunta = st.chat_input("Pergunte algo sobre finanças:")
if pergunta:
    st.chat_message("user").write(pergunta)

    with st.spinner("Lumi está pensando..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
