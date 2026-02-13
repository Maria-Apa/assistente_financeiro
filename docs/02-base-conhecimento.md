# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Modifiquei o arquivo produtos_financeiros, adicionando algumas novas modalidades de investimentos, como Renda+, Educa+, CDB de 6 meses e 1 ano e Fundos Imobiliários. Esses produtos adicionais foram adicionados para deixar o projeto mais completo e para que o assistente possa ter mais conhecimento dos produtos que ele poderá explicar. Além dessas informações, também acrescentei a informação de resgate das modalidades de investimento, para que as informações fiquem mais completas. 

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades, injetar os dados diretamente no prompt (ctrl + c, ctsl + v) ou carregar os arquivos via código, como no exemplo abaixo: 

```python
import pandas as pd
import java

# CVS
histórico = pd.read_csv('data/historico_atendimento.csv')
transações = pd.read_csv('data/transacoes.csv')

#JSONs
with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
	perfil = json.load(f)

with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
	perfil = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar, podemos simplesmente "injetar" os dados em nosso prompt, garantindo que o Agente tenha o melhor contexto possível. Lembrando que, as soluções mais robustas, , o ideal é que essas informações sejam carregadas dinamicamente para que possamos ganhar flexibilidade. 

```text

PERFIL DO CLIENTE (perfil_investidor.json):

{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSAÇÕES DO CLIENTE (transacoes.csv):

data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

HISTORICO DE ATENDIMENTO DO CLIENTE (historico_atendimento.csv):

data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

PRODUTOS DISPONIVEIS (produtos_financeiros.json):

[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes",
    "resgate": "Dias úteis"
  },

    {
    "nome": "Tesouro Renda+ Aposentadoria",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "IPCA + 7.26% a.a",
    "aporte_minimo": 18.97,
    "indicado_para": "Renda Extra do Tesouro para a aposentadoria",
    "resgate": "Após 60 dias"
  },

    {
    "nome": "Tesouro Educa+",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "IPCA + 7.69% a.a",
    "aporte_minimo": 18.97,
    "indicado_para": "Renda Extra usada para fins educacionais",
    "resgate": "Após 60 dias"
  },
  
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 10.00,
    "indicado_para": "Quem busca segurança com rendimento diário",
    "resgate": "Diario"
  },

    {
    "nome": "CDB 6 meses",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "108% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca guardar o dinheiro com segurança, mas sem retirar o valor antes do periodo de 6 meses",
    "resgate": "No Vencimento"
  },

  {
    "nome": "CDB 1 ano",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "112% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca guardar o dinheiro com segurança, mas sem retirar o valor antes do periodo de 12 meses",
    "resgate": "No Vencimento"
  },
  
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)",
    "resgate": "Após 90 dias"
  },
  
    {
    "nome": "Fundo Imobiliario (FII)",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "Dividend Yield (DY), costuma girar entre 7% e 12% ao ano",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil moderado que busca diversificação e renda recorrente mensal",
    "Pagamento_resgate": "Até D+5"
  },
  
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação",
    "Pagamento_resgate": "Até D+5"
  },
  
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
    "Pagamento_resgate": "Até D+5"
  }
]

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo de contexto montado abaixo, se baseia nos dados originais da base de conhecimento, mas os sintetiza deixando apenas as informações mais relevantes, otimizando assim o consumo de tokens. Entretanto, vale lembrar que mais importante do que economizar tokens, é ter todas as informações relevantes disponíveis em seu contexto. 

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

RESUMO DE GASTOS: 
- Moradia: R$ 1.380
- Alimentação: R$ 570
- Transporte: R$ 295
- Saldo: R$ 188
- Lazer: R$ 55,98
- Total de saída: R$ 2.488,90

- Tesouro Selic
- Tesouro Renda+
- Tesouro Educa+
- CDB Liquidez Diário
- CDB 6 meses
- CDB 1 ano
- LCI/LCA
- Fundo Imobiliario (FII)
- Fundo Multimercado
- Fundo de Ações
```
