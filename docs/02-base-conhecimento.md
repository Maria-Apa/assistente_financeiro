# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `perfil_investidor.json` | JSON | Identificar o perfil do investidor e orientar recomendações personalizadas |
| `produtos_financeiros.json` | JSON | Listar e explicar produtos financeiros adequados ao perfil e objetivo do usuário |
| `riscos_financeiros.json` | JSON | Apresentar os principais riscos associados a cada tipo de investimento |
| `info_financeira.json` | JSON | Fornecer conceitos e informações financeiras de suporte para respostas mais claras |
| `tributacao_financeira.json` | JSON | Explicar as regras de tributação aplicadas a cada produto financeiro |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Sim, eu expandi os dados mockados no sistema e realizei algumas modificações:

* perfil_investidor.json <br>
Adicionei perguntas para identificar o perfil do investidor (conservador, moderado ou arrojado). Essas perguntas permitem oferecer explicações e recomendações alinhadas aos objetivos do usuário.

* produtos_financeiros.json <br>
Ampliei a lista de investimentos, incluindo Tesouro Renda+ Aposentadoria, Tesouro Educa+, CDB de prazo fechado, Fundo Imobiliário (FII) e outros tipos de CDB. Também inseri informações complementares, como regras de resgate.

* riscos_financeiros.json, info_financeira.json e tributacao_financeira.json <br>
Esses arquivos foram criados do zero, com conteúdos estruturados sobre conceitos financeiros, visando aprimorar as explicações do assistente, reforçar a precisão das respostas e reduzir riscos de alucinação.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades, injetar os dados diretamente no prompt (ctrl + c, ctsl + v) ou carregar os arquivos via código, como no exemplo abaixo: 

```python
import json
import pandas as pd
import streamlit as st
from groq import Groq
import calculo_financeiro as cf
import re

# ============= CONFIGURAÇÃO =============
client = Groq(api_key="Sua_Chave)
MODELO = "llama-3.1-8b-instant"

# ============= CARREGAR DADOS =============
# Removidos: perfil, transacoes, historico
produtos = json.load(open('./data/produtos_financeiros.json', encoding='utf-8'))
info_financeira = json.load(open('./data/info_financeira.json', encoding='utf-8'))
riscos_financeiros = json.load(open('./data/riscos_financeiros.json', encoding='utf-8'))
tributacao_financeira = json.load(open('./data/tributacao_financeira.json', encoding='utf-8'))
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar, os dados podem ser injetados diretamente no system prompt, garantindo que o agente tenha todo o contexto necessário já no início da conversa.
No entanto, em soluções mais robustas, o ideal é que essas informações sejam carregadas dinamicamente via código, permitindo maior flexibilidade, atualização fácil dos arquivos JSON e redução do tamanho do prompt.

```text
========= PERFIL INVESTIDOR perfil_investidor.json: =========
{
  "perfis": [
    {
      "id": "conservador",
      "nome": "Conservador",
      "descricao": "Prioriza segurança, estabilidade e preservação do patrimônio. Evita oscilações e prefere investimentos de baixo risco.",
      "caracteristicas": [
        "Baixa tolerância ao risco",
        "Busca previsibilidade",
        "Prefere liquidez",
        "Aceita rendimentos menores para ter mais segurança"
      ],
      "investimentos_adequados": [
        "CDB com liquidez diária",
        "Tesouro Selic",
        "LCI/LCA"
      ],
      "perguntas_diagnostico": [
        "Qual sua tolerância a oscilações nos investimentos?",
        "Quanto de segurança você considera importante?",
        "Qual o seu objetivo principal: segurança ou rendimento?",
        "Qual o seu horizonte de tempo para investir?"
      ]
    },
    {
      "id": "moderado",
      "nome": "Moderado",
      "descricao": "Busca equilibrar segurança e rentabilidade. Aceita alguma oscilação para ter melhores retornos no médio prazo.",
      "caracteristicas": [
        "Tolerância intermediária ao risco",
        "Busca equilíbrio entre segurança e retorno",
        "Aceita volatilidade moderada",
        "Foca em médio e longo prazo"
      ],
      "investimentos_adequados": [
        "CDB de prazo fechado",
        "Tesouro IPCA+",
        "Fundos Multimercado leves"
      ],
      "perguntas_diagnostico": [
        "Você aceita pequenas oscilações para buscar maiores retornos?",
        "Seu objetivo é curto, médio ou longo prazo?",
        "Qual porcentagem do patrimônio você está disposto a arriscar?",
        "Você já investiu antes em algo além da poupança?"
      ]
    },
    {
      "id": "arrojado",
      "nome": "Arrojado",
      "descricao": "Focado em rentabilidade mais alta, aceita riscos maiores e oscilações fortes ao longo do caminho.",
      "caracteristicas": [
        "Alta tolerância ao risco",
        "Busca retornos elevados",
        "Aceita volatilidade intensa",
        "Pensa no longo prazo"
      ],
      "investimentos_adequados": [
        "Ações",
        "FIIs",
        "Fundos Multimercado"
      ],
      "perguntas_diagnostico": [
        "Você está confortável com grandes oscilações no curto prazo?",
        "Qual seu foco: crescimento forte do patrimônio ou estabilidade?",
        "Você tem reserva de emergência formada?",
        "Qual o prazo mínimo que você pretende manter os investimentos?"
      ]
    }
  ]
}

========= PRODUTOS FINANCEIROS produtos_financeiros.json: =========

[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "Mercado, Liquidez e Crédito, porém é baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes",
    "resgate": "Liquidez Diária"
  },

    {
    "nome": "Tesouro Renda+ Aposentadoria",
    "categoria": "renda_fixa",
    "risco": "Mercado, Liquidez e Crédito, porém é baixo",
    "rentabilidade": "IPCA + 7.26% a.a",
    "aporte_minimo": 18.97,
    "indicado_para": "Renda Extra do Tesouro para a aposentadoria",
    "resgate": "Após 60 dias"
  },

    {
    "nome": "Tesouro Educa+",
    "categoria": "renda_fixa",
    "risco": "Mercado, Liquidez e Crédito, porém é baixo",
    "rentabilidade": "IPCA + 7.69% a.a",
    "aporte_minimo": 18.97,
    "indicado_para": "Renda Extra usada para fins educacionais",
    "resgate": "Após 60 dias"
  },
  
  {
    "nome": "CDB (Certificado de Depósito Bancário) Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI (Certificado de Depósito Interbancário)",
    "aporte_minimo": 10.00,
    "indicado_para": "Quem busca segurança com rendimento diário",
    "resgate": "Liquidez Diária"
  },


  {
    "nome": "CDB (Certificado de Depósito Bancário) prazo fechado 1 ano",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "112% do CDI (Certificado de Depósito Interbancário)",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca guardar o dinheiro com segurança, mas sem retirar o valor antes do periodo de 12 meses",
    "resgate": "No Vencimento, prazo fechado"

  },
  
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI (Certificado de Depósito Interbancário)",
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
    "rentabilidade": "CDI (Certificado de Depósito Interbancário) + 2%",
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
    "indicado_para": "Perfil arrojado com foco no longo prazo",
    "Pagamento_resgate": "Até D+5"
  }
]

========= RISCOS FINANCEIROS riscos_financeiros.json: =========

{
    "Risco_de_Mercado":{
        "descricao": "O risco de mercado é a possibilidade de perdas financeiras em investimentos devido à oscilação de preços e taxas no mercado, gerada pela volatilidade, eventos econômicos, políticos ou naturais.",
        "caracteristicas_e_fatores": [
            "Causas: Mudanças nas taxas de juros, variações cambiais, crises políticas, guerras e desastres naturais.",
            "Impacto: Desvalorização de ativos (ex: ações caindo, título prefixado perdendo valor se juros subirem).",
            "Gestão: Envolve definir limites de risco, diversificar carteiras e monitorar indicadores econômicos para minimizar perdas. ",
            "Mensuração: Utiliza-se frequentemente o Value at Risk (VaR), que estima a perda máxima esperada em um determinado horizonte de tempo e confiança."
        ],

        "possuem_risco": [
            "Fundos Imobiliários (FIIs): relacionado com a variação do preço das cotas.",
            "Fundos de Investimento (Ações, Multimercado)",
            "Renda Fixa"
        ]
    },
    
    "Risco_de_Liquidez":{
        "descricao": "O Risco de Liquidez é a possibilidade de não conseguir vender um ativo financeiro rapidamente pelo seu preço justo, resultando em perdas financeiras ou necessidade de aceitar uma desvalorização para concretizar a venda. Ele afeta a capacidade de transformar investimentos em dinheiro e é comum em ativos de baixa negociação, como imóveis, ou resgates antecipados em renda fixa. ",
        "principais_aspectos": [
            "Definição: É a dificuldade de conversão de um ativo em dinheiro sem perda significativa de valor.",
            "Impacto no preço: Ativos com alto risco de liquidez podem exigir grandes descontos (spreads altos) para serem vendidos rapidamente.",
            "Exemplos de Baixa Liquidez: Imóveis, obras de arte, títulos de crédito privado de pequenas empresas ou ações de empresas pouco negociadas.",
            "Exemplos de Alta Liquidez: Dinheiro em conta, tesouro direto, ações de grandes empresas (blue chips).",
            "Risco de Financiamento: Refere-se à dificuldade de uma entidade cumprir suas obrigações de curto prazo por falta de caixa, mesmo que possua ativos." 
        ],

        "possuem_risco": [
            "Renda Fixa com Prazo Fechado",
            "Fundos Imobiliários (FIIs): as cotas dos FII são fechadas, não tem resgate. Mas, apesar de não ter resgate é possível encontrar liquidez no mercado e o risco está em encontrar compradores para as cotas quando quiser vender.",
            "Fundos de Investimento Fechados",
            "Fundo Multimercado"
        ]
    },

    "Risco_de_Crédito":{
        "descricao": "Risco de crédito (ou risco de calote) existe em investimentos onde o emissor pode não honrar o pagamento, sendo mais alto em ativos de renda fixa privada sem a garantia do Fundo Garantidor de Créditos (FGC).",
        "principais_aspectos": [
            "Gestão: Envolve originação, análise, monitoramento e cobrança para reduzir perdas.",
            "Aplicação: Presente em empréstimos, financiamentos, vendas a prazo e investimentos de renda fixa.",
            "Probabilidade de Inadimplência: Quanto maior o risco, maior a remuneração (spread) exigida para compensar o investidor."
        ],

        "possuem_risco": [
            "Renda Fixa",
            "Fundos de Crédito Privado",
            "Fundos Imobiliários (FIIs): presente nos Fundos de Papel, o FII além de comprar imóveis também pode investir em papéis, como por exemplo, CRI, LCI, CCI, LIG, ou seja, ativos que estão atrelados ao mercado imobiliário.",
            "Fundo Multimercado"
        ]
    },

    "Risco_de_Vacância": {
        "descricao": "O risco de vacância é a possibilidade de um imóvel ou portfólio imobiliário ficar desocupado, resultando em perda de receita de aluguel e custos de manutenção sem geração de renda. Ele é um indicador crucial para Fundos Imobiliários (FIIs), impactando diretamente a distribuição de dividendos e reduzindo o valor patrimonial dos ativos. ",
        "pontos_chave": [
            "Tipos: Existe a vacância física (área desocupada) e a vacância financeira (inadimplência ou contratos renegociados que geram menos renda), segundo Investidor10 e Toro Investimentos.",
            "Impacto no Fluxo de Caixa: Imóveis vazios não geram aluguel, mas geram custos fixos (IPTU, condomínio, manutenção).",
            "Consequências: Alta vacância reduz o lucro do investidor, baixa o valor do ativo e pode pressionar o preço do aluguel para baixo devido ao aumento da concorrência, conforme a ABECIP e a Empiricus.",
            "Fatores de Risco: Localização ruim, má qualidade do ativo, cenários econômicos desfavoráveis e fim de contratos longos, apontam a Suno e o Ativore Asset. "
        ],
        
        "possui_risco": [
            "Fundo Multimercado",
            "Fundo Imobiliario (FII)"
        
        ]
    }

}

========= INFORMAÇÕES FINANCEIRAS info_financeira.json: =========

{
  "CDI": {
    "nome": "Certificado de Depósito Interbancário",
    "descricao": "O CDI é a taxa média das operações de empréstimo entre bancos. As instituições financeiras emprestam dinheiro entre si diariamente para fechar o caixa. No fim do dia, a média dessas operações determina a taxa CDI.",
    "relacao_selic": "Se um banco não conseguir captar recursos no mercado interbancário, ele usa a taxa Selic Over como referência. Por isso, o CDI acompanha a Selic muito de perto.",
    "usos": [
      "Referência para investimentos de renda fixa",
      "Cálculo de rendimento de CDBs, LCIs, LCAs e fundos DI",
      "Indicador para operações interbancárias"
    ]
  },

  "SELIC": {
    "nome": "Sistema Especial de Liquidação e Custódia",
    "descricao": "A taxa Selic é a taxa básica de juros da economia brasileira, definida pelo Banco Central.",
    "funcao": "Serve como principal referência para todas as taxas de juros do país, influenciando crédito, financiamentos e investimentos.",
    "tipos": [
      "Selic Meta — definida pelo Copom",
      "Selic Over — taxa efetiva das operações garantidas por títulos públicos"
    ]
  },

  "IPCA":{
    "nome": "Índice Nacional de Preços ao Consumidor Amplo",
    "descricao": "é o índice oficial de inflação do Brasil, calculado mensalmente pelo IBGE desde 1979. Ele mede a variação de preços de produtos e serviços consumidos por famílias com rendimentos de 1 a 40 salários mínimos, abrangendo cerca de 90% da população urbana. É a referência para as metas de inflação do Banco Central. ",
    "usos": [
        "É a referência oficial utilizada pelo Conselho Monetário Nacional (CMN) para definir as metas de inflação que o Banco Central do Brasil deve seguir.",
        "Serve como base para a correção anual de contratos, incluindo aluguéis, planos de saúde, mensalidades escolares e tarifas públicas.",
        "É o indexador de títulos de renda fixa 'híbridos', como o Tesouro IPCA+, garantindo que o rendimento supere a inflação e mantenha o poder de compra.",
        "Analistas e governos utilizam o IPCA para medir a saúde econômica do país e o impacto no custo de vida das famílias (com rendimentos de 1 a 40 salários mínimos). "
    ]
  },

  "Liquidez_diaria": {
    "descricao": "Liquidez diária, ou imediata, é a capacidade de resgatar um investimento a qualquer momento em dias úteis, com o dinheiro disponível na conta no mesmo dia (D+0) ou no próximo (D+1). É o ideal para reservas de emergência e objetivos de curto prazo, oferecendo alta segurança, flexibilidade e rentabilidade diária, sem carência. ",
    "caracteristicas": [
        "Resgate Rápido: Acesso ágil ao capital, sem necessidade de esperar vencimentos ou carências.",
        "Ideal para Emergências: Perfeito para construir a reserva de emergência, permitindo uso imediato em imprevistos.",
        "Rendimento: Diferente da conta corrente, o dinheiro continua rendendo proporcionalmente a cada dia, geralmente atrelado ao CDI. "
    ]
  },

    "FGC":{
        "nome": "Fundo Garantidor de Crédito",
        "descricao": "O Fundo Garantidor de Créditos (FGC) é uma associação civil privada, sem fins lucrativos, que atua como um seguro para depositantes e investidores no Brasil. Ele protege até R$ 1 milhão, a cada 4 anos, em caso de falência ou intervenção do Banco Central em bancos associados. ",
        "principais_aspectos": [
            "Objetivo: Aumentar a confiança e estabilidade do Sistema Financeiro Nacional, protegendo correntistas e investidores.",
            "Produtos Cobertos: Depósitos à vista (conta corrente), poupança, CDBs, RDBs, LC, LH, LCI, LCA e LCD.",
            "Cobertura: R$ 250.000,00 por CPF ou CNPJ, por conjunto de instituições do mesmo conglomerado financeiro.",
            "Funcionamento: Financiar a proteção através de contribuições mensais dos bancos associados, não utilizando recursos públicos.",
            "Prazo de Pagamento: Geralmente ágil, com médias recentes reduzidas para poucos dias úteis após a lista de credores ser fornecida pelo interveniente. "
        ]
    },

    "Fundo_de_investimento": {
        "descricao": "Um fundo de investimento é uma forma coletiva de aplicação financeira, funcionando como um 'condomínio' onde diversos investidores (cotistas) unem recursos para aplicar em ativos como ações, renda fixa, imóveis ou câmbio. Geridos por profissionais, oferecem diversificação, praticidade e acesso a diferentes mercados, com rendimentos proporcionais às cotas possuídas.",
        "caracteristicas": [
            "Cotistas: Os investidores compram cotas, representando uma fração do patrimônio total.",
            "Custos: Geralmente, cobram taxa de administração (gestão) e, em alguns casos, taxa de performance (para resultados acima do esperado).",
            "Regulação: São fiscalizados pela Comissão de Valores Mobiliários (CVM). "
        ],
        "tipificacao":  [
            "Renda fixa, Cambial, Multimercados, Ações, Incentivados em infraestrutura e Garantia de locação imobiliária, Fundo Imobiliário"
        ],
        "vantagem": "Diversificação imediata, gestão profissional, facilidade de acesso, liquidez (em fundos abertos) e diversificação de riscos.",
        "custos": [
            "Taxa de Administração: Taxa fixa, expressa em percentual ao ano, cobrada e deduzida diariamente do patrimônio líquido da classe. A cobrança de taxa de administração afeta o valor da cota. ",
            "Taxa de entrada ou ingresso: taxa paga pelo cotista ao patrimônio da classe ao aplicar recursos em uma classe de cotas, pouco utilizada. ",
            "Taxa de saída: taxa paga pelo cotista ao patrimônio da classe ao resgatar recursos de uma classe de cotas, também é pouco utilizada. ",
            "Taxa de distribuição de cotas: taxa cobrada do fundo, representativa do montante total para remuneração dos distribuidores.",
            "Taxa de gestão: taxa cobrada do fundo para remunerar o gestor e os prestadores de serviços por ele contratados e que não constituam encargos do fundo.",
            "Taxa de performance: possibilidade de cobrança dessa taxa pelo gestor, percentual cobrado em razão do resultado positivo da classe. Só é cobrada quando o fundo tiver uma performance muito boa."
        ],
        "prestadores_de_servico": [
            "Administrador",
            "Gestor",
            "Distribuidor",
            "Tesouraria",
            "Custodiante / Escriturador",
            "Auditor independente"
        ],
        "fundo_imobiliario": {
            "descricao": "Os Fundos Imobiliários (FII) são fundos de investimento fechados destinados à aplicação em empreendimentos imobiliários, o que inclui, além da aquisição de direitos reais sobre bens imóveis, o investimento em títulos relacionados ao mercado imobiliário como, por exemplo, LCI e CRI. ",
            "caracteristicas": [
                "São fundos fechados que podem ter duração determinada ou indeterminada",
                "Objeto de oferta pública na emissão. Então, quando o FII vai emitir novas cotas, já que é um fundo fechado, passa por todo o processo de oferta pública (registro na CVM, consórcio de distribuição ...)",
                "Pode ser negociado na bolsa de valores ou mercado de balcão."
            ]
        }
        
    },
    
    "Administrador": {
        "descricao": "O administrador de fundos de investimento é a instituição responsável legalmente pela constituição, funcionamento, fiscalização e conformidade regulatória do fundo perante a CVM (Comissão de Valores Mobiliários, garantindo os direitos dos cotistas.",
        "pode_contratar": [
            "Serviço de Tesouraria (cuidar do caixa do fundo)",
            "Escrituração de cotas (instituição que irá controlar o registro das cotas, também chamado de custodiante).",
            "Auditoria independente: contratação obrigatória, irá fazer a auditoria das demonstrações contábeis do fundo."  
        ],
        "atribuicoes": [
            "Supervisionar as operações realizadas pelo gestor, se está de acordo com a política de investimento da classe e dentro dos limites de concentração.",
            "Gestão do risco de liquidez do fundo, que deve ser feita em conjunto com o gestor de recursos (anota isso aqui tá? É muito importante).",
            "Observar as disposições constantes do regulamento.",
            "Apreçamento dos ativos que compõem a carteira dos veículos de investimento.",
            "Cumprir as deliberações da assembleia de cotistas. O administrador é quem administra o fundo, ele não é dono do fundo, portanto ele precisa seguir as regras.",
            "Manter atualizada junto à CVM a lista de todos os prestadores de serviços contratados pelo fundo e as demais informações cadastrais do fundo e suas classes de cotas.",
            "Diligenciar para que sejam mantidos, atualizados e em perfeita ordem: o registro de cotistas; o livro de atas das assembleias gerais; o livro ou lista de presença de cotistas; os pareceres do auditor independente e os registros contábeis referentes às operações e ao patrimônio do fundo.",
            "O administrador é responsável por publicar, em seu site na internet, todas as informações relevantes do fundo de investimento."
        ]
    },

    "Gestor": {
        "descricao": "O gestor de fundos é o profissional responsável por administrar os recursos de terceiros em fundos de investimento, tomando decisões estratégicas de compra, venda e alocação de ativos (ações, renda fixa, imóveis) para maximizar retornos, seguindo o regulamento do fundo. Eles analisam o mercado, gerenciam riscos e definem a estratégia, seja ela ativa (bater o índice) ou passiva (replicar o índice). ",
        "pode_contratar": [
            "Distribuidor: responsável por vender as cotas do fundo de investimento a mercado.",
            "Classificadora de risco: uma agência classificadora de risco irá classificar o risco do emissor de determinado título de crédito",
            "Cogestão da carteira: contratar um outro gestor, sendo comum em fundos que possuem muitas classes de cotas. Então cada gestor cuida de uma classe de cotas por exemplo"
        ],
        "atribuicoes": [
            "Responsável pela observância dos limites de composição e concentração de carteira e de concentração em fatores de risco.",
            "Fornecer aos distribuidores todo o material de divulgação da classe de cotas.",
            "Informar aos distribuidores qualquer alteração que ocorra na classe, especialmente se decorrente da mudança do regulamento",
            "Comunicar a CVM o fechamento de cotas para resgate (sim, as vezes o fundo pode fechar para resgate. Mas veremos mais detalhes depois)",
            "Exercer o direito de voto decorrente de ativos detidos pela classe. Por exemplo se o gestor comprou as ações da empresa T2SA3, na assembleia de acionista dessa empresa, o gestor pode votar representando o interesse do fundo.",
            "Manter atualizada a documentação relativa às operações da classe de cotas",
            "Gestão de risco dos veículos de investimento, incluindo, mas não se limitando, pela gestão do risco de liquidez em conjunto com o administrador fiduciário",
            "Garantir que as operações realizadas pelos veículos de investimento (Fundo de Investimento) tenham sempre propósitos econômicos compatíveis com os documentos dos veículos de investimento, e estejam em consonância com os princípios gerais de conduta previstos no código de administração e gestão de recursos de terceiros da Anbima.",
            "Manter a carteira de ativos enquadrada aos limites de composição e concentração e, se for o caso, de exposição ao risco de capital",
            "Cumprir as deliberações da assembleia de cotistas"
        ]
    }
  
}

========= TRIBUTAÇÃO tributacao_financeira.json =========

{
  "IR_Renda_Fixa":{
    "nome": "Imposto de Renda",
    "descricao": "os investimentos de Renda Fixa são tributados com Imposto de Renda (IR), a cobrança desse tributo será feita conforme uma tabela regressiva",
    "tabela": [
        "No período de até 180 dias a alíquota é 22,50%",
        "No período de 180 a 360 dias a alíquota é 20%",
        "No período de 361 a 700 dias a alíquota é 17,5%",
        "No período acimda de 700 dias a alíquota é 15%"
        ],
    "importante": "IR é cobrado sobre o rendimento líquido de IOF."
  },

  "IOF_Renda_Fixa":{
    "nome": "IMPOSTO SOBRE OPERAÇÕES FINANCEIRAS",
    "descricao": "Os rendimentos obtidos em títulos de Renda Fixa, justamente por terem um prazo definido no momento do investimento, serão tributados com IR (imposto de renda) e IOF regressivo. No caso do IOF terá uma tabela que isenta o investidor a partir do 30º dia. Isto é, investimentos realizados com prazo de resgate inferior ou igual 30 dias serão tributados de acordo com Tabela Regressiva",
    "tabela": [
        { "dias": "1 a 6", "percentual": "96% a 80%" },
        { "dias": "7 a 14", "percentual": "76% a 53%" },
        { "dias": "15 a 20", "percentual": "50% a 33%" },
        { "dias": "21 a 30", "percentual": "30% a 0%" }
    ]
    },
    
   "tributacao_fundos_investimentos": {
    "descricao": "A tributação está relacionada com a tipificação. A receita federal reconhece que existem dois tipos de fundos.",
    "iof": [
        "Fundos de renda fixa, cambial e multimercados estão sujeitos ao IOF de acordo com a tabela regressiva.",
        "Fundo com carência tem alíquota de 0,5% ao dia de IOF caso o investidor resgate antes do vencimento da carência. "
        ],
        
    "aliquota_unica": [
        "o fundo de infraestrutura, o investidor pessoa física está isento de IR e o investidor pessoa jurídica pagará uma alíquota de 15% no resgate.",
        "O fundo de ações e o fundo de investimento em participações (private equity) são tributados com alíquota única de 15% no resgate. "
        ],

    "fundos_com_ir": {
        "curto_prazo": [
            "prazo médio da carteira igual ou inferior a 365 dias. Sendo: Até 180 dias aliquota de 22,50% e acima de 180 dias a aliquota é 20%",
            "De acordo com a CVM, para ser classificado como fundo de curto prazo é necessário: Prazo médio da carteira inferior a 60 dias ou prazo máximo de vencimento do ativo inferior a 375 dias.",
            "Mas para fins de tributação, a receita federal considera que um fundo de curto prazo tem o prazo médio da carteira igual ou inferior a 365 dias. "
            ],

        "longo_prazo": "prazo médio da carteira superior a 365 dias. Segue a tabela regressiva do IR.",
        "Fundos": "Os fundos de renda fixa, cambial, multimercado e fundo de investimento em direitos creditórios, serão tributados de acordo com a tabela regressiva e o tempo de permanência do investidor"
        },

    "come_cotas": [
        "Come-cotas é o nome que se dá para uma antecipação no recolhimento do Imposto de Renda em classes de cotas de renda fixa, cambial e multimercados do tipo aberto. Em outras palavras, o fundo de investimento recolhe o IR da valorização das cotas a cada 6 meses, independentemente do resgate.",
        "Será cobrada sempre nos últimos dias úteis de maio e novembro.",
        "Será cobrada SEMPRE uma alíquota fixa (classe de curto prazo, 20%; classe de longo prazo, 15%)",
        "Recolhida pelo administrador",
        "Exceção: Classes de cota que têm carência para resgate maior que 90 dias o come cotas será cobrado no vencimento da carência. "
        ],
    
    "fundo_imobiliario": [
        "Ganho de capital: 20% para PF, PJ e até mesmo para PJ isento. Recolhido pelo próprio investidor via DARF. O investidor terá até o último dia útil do mês subsequente para realizar o recolhimento",
        "Rendimento (dividendo): isento de IR para PF, PJ é 20%, retido na fonte. "
        ]
    }

}


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
