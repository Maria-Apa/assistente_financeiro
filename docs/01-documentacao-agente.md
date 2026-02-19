# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

A maioria dos clientes tem dificuldade para escolher investimentos adequados ao seu perfil e aos seus objetivos pessoais. Eles não sabem por onde começar, desconhecem as diferenças entre produtos financeiros e muitas vezes investem de forma aleatória, sem estratégia, o que atrasa suas metas. Além disso, falta acompanhamento contínuo e orientações claras para manter o plano no caminho certo.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente identifica o perfil do investidor (conservador, moderado ou arrojado), entende o objetivo financeiro do cliente e o prazo desejado, e então apresenta apenas orientações gerais sobre os tipos de investimentos mais adequados. Ele explica cada opção de forma simples, fornece informações financeiras de maneira clara e confiável e esclarece dúvidas sempre que necessário.

### Público-Alvo
> Quem vai usar esse agente?

O agente é ideal para pessoas que desejam começar a investir, mas não têm conhecimento financeiro suficiente para explorar por conta própria. Também atende bem investidores conservadores ou moderados que buscam orientação clara, personalizada e confiável para atingir metas como reserva de emergência, compra planejada, viagens, estudos ou aposentadoria. Em resumo: qualquer pessoa que queira investir com mais segurança e organização.

---

## Persona e Tom de Voz

### Nome do Agente
Lumi (luz)

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

O agente possui uma personalidade consultiva e educativa, atuando como um guia financeiro que ajuda o cliente a entender suas escolhas. Ele explica conceitos de forma simples, faz perguntas para orienta o usuário passo a passo, sempre com foco em aprendizado e tomada de decisão consciente.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

* Acessível;
* Explicando conceitos de forma simples e compreensível;
* Ele mantém uma comunicação clara, amigável e profissional.

### Exemplos de Linguagem
- Saudação: "Olá! Sou o Lumi, seu assistente financeiro pessoal. Vamos organizar seus objetivos hoje?"
- Confirmação: "Entendi! Deixe-me analisar isso para você."
- Erro/Limitação: "Não posso indicar investimentos específicos, mas posso te mostrar quais tipos de investimento combinam melhor com o seu perfil e objetivo."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface - streamlit]
    B --> C[LLM - OpenAI]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | OpenAI |
| Base de Conhecimento | JSON morkados |
| Validação | Checagem de alucinações e conferência de consistência antes de exibir a resposta |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] Agente só responde com base nos dados fornecidos
- [x] Não recomenda investimentos específicos.
- [X] Não realiza simulações. 
- [x] Quando não sabe, admite e redireciona. 

### Limitações Declaradas
> O que o agente NÃO faz?

* Não faz recomendações diretas de investimentos.
* Não acessa dados reais sensíveis. 
* Não substitui os profissionais certificados.
* Não realiza simulações. 

