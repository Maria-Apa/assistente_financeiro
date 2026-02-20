# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação única
```

## Exemplo de requirements.txt

```
streamlit
OpenAI
python-dotenv
```
## Passo a Passo da Execução

1. Crie a estrutura de pastas do projeto

  - Crie uma pasta chamada "Lumi".
  - Dentro dela, crie a pasta "data" e coloque todos os arquivos .json.
  - Crie também a pasta "src" e coloque dentro dela o código do assistente (por exemplo, app.py).

2. Criar a chave da API na OpenAI

  - Acesse: https://platform.openai.com/
  - Faça login ou crie uma conta.
  - No menu lateral, clique em "API Keys". (Necessário pagamento)
  - Clique em "Create new secret key".
  - Copie a chave que foi gerada.
  - Adicione em:

```
client = OpenAI(api_key="SUA_CHAVE")
```
  - No terminal, execute o comando para iniciar o Lumi:
```
streamlit run .\src\app.py
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run .\src\app.py
```

## Evidência

<img width="1724" height="862" alt="image" src="https://github.com/user-attachments/assets/9e7c4a7f-3516-4c7a-b1d3-94c376dba9b3" />





