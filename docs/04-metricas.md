# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Quais são os tipos de produtos para um perfil moderado? |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | Avalia se a resposta está alinhada ao perfil do usuário e com as regras definidas. | Usuário conservador pergunta por opções; o agente responde apenas categorias adequadas ao perfil |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de produto
- **Pergunta:** "O que é um CDB?"
- **Resposta esperada:** Explicação simples, baseada no `produtos_financeiros.json`, sem inventar taxas.
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Solicita mais informações para que possa prosseguir. 
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto qual o valo de um Bitcoin?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [ ] Correto  [X] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O assistente identifica corretamente os tipos de investimentos presentes nos arquivos JSON.
- Antes de apresentar sugestões, ele solicita mais informações sobre o perfil do usuário (como conservador, moderado ou arrojado).
- Ele lida bem com perguntas fora do contexto financeiro, como previsão do tempo, informando que não possui essa informação.

**O que pode melhorar:**
- O assistente ainda cria algumas informações que não estão na sua base de conhecimento.
Por exemplo: ao ser questionado “Qual o valor de um Bitcoin?”, ele corretamente responde que não possui essa informação, mas em seguida começa a explicar o que é Bitcoin, mesmo sem haver dados sobre isso na base.


