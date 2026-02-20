# 🌟 Lumi — Seu Assistente Financeiro Educativo

## Contexto

O Lumi é um agente inteligente desenvolvido para democratizar o acesso à educação financeira. Ele ajuda investidores iniciantes a identificar seu perfil, entender produtos financeiros e tirar dúvidas sem julgamentos, transformando o "medo de perguntar" em decisões conscientes.
Ele possui capacidade para: 

- **Orientar sobre investimentos** ao invés de apenas responder perguntas
- **Personalizar** sugestões com base no contexto/perfil de cada cliente
- **Garantir segurança** e confiabilidade nas respostas (anti-alucinação)

---

## O Problema

Muitos clientes sentem vergonha de buscar orientação financeira por medo de fazer "perguntas bobas". Isso gera dois comportamentos perigosos:

- **Inércia:** O cliente deixa de investir por insegurança.
- **Escolhas Erradas:** O cliente busca informações externas sem curadoria e acaba em produtos inadequados ao seu perfil de risco.

---

## A Solução

O Lumi atua como um guia consultivo e educativo. Através de uma linguagem acolhedora e simples, ele:

- Identifica se o usuário é Conservador, Moderado ou Arrojado.
- Explica conceitos como CDI, SELIC, IPCA e Liquidez.
- Apresenta categorias de investimentos (CDB, Tesouro, LCI/LCA, FIIs) baseadas estritamente em uma base de dados segura.

---
## Tecnologias Utilizadas

## Ferramentas Utilizadas

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | [ChatGPT](https://chat.openai.com/)|
| **Desenvolvimento** | [Streamlit](https://streamlit.io/)|
| **Diagramas** | [Mermaid](https://mermaid.js.org/)|

---

### 2. Base de Conhecimento

Utilizei os **dados mockados** disponíveis na pasta [`data/`](./data/) para alimentar meu agente:

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `info_financeira.json` | JSON | Histórico de transações do cliente |
| `perfil_investidor.json` | JSON | Histórico de atendimentos anteriores |
| `produtos_financeiros.json` | JSON | Perfil e preferências do cliente |
| `riscos_financeiros.json` | JSON | Produtos e serviços disponíveis |
| `tributacao.json` | JSON | Produtos e serviços disponíveis |


📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documente os prompts que definem o comportamento do seu agente:

- **System Prompt:** Instruções gerais de comportamento e restrições
- **Exemplos de Interação:** Cenários de uso com entrada e saída esperada
- **Tratamento de Edge Cases:** Como o agente lida com situações limite

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Desenvolva um **protótipo funcional** do seu agente:

- Chatbot interativo (sugestão: Streamlit, Gradio ou similar)
- Integração com LLM (via API ou modelo local)
- Conexão com a base de conhecimento

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Descreva como você avalia a qualidade do seu agente:

**Métricas Sugeridas:**
- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Coerência com o perfil do cliente

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Grave um **pitch de 3 minutos** (estilo elevador) apresentando:

- Qual problema seu agente resolve?
- Como ele funciona na prática?
- Por que essa solução é inovadora?

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── info_financeira.json          # Informação Financeira
│   ├── perfil_investidor.json        # Perfil do Investidor
│   ├── produtos_financeiros.json     # Produtos Financeiros
|   ├── riscos_financeiros.json       # Riscos Financeiros
│   └── tributacao.json               # Tributação
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # Código em Python
│
├── 📁 assets/                        # Imagens do Assistente
│   └── ...
└──  README.md
```


