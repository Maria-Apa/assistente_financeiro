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
groq
python-dotenv
```
## Passo a Passo da Execução

- Criar uma pasta "Lumi",
- Baixar a pasta "Data",
- Criar uma pasta "src",
- Adicione no Lumi,
- Crias uma conta no groq.com;
- Acessar API Keys;
- Clicar em "CREATE API KEY";
- Copiar a Chave;
- Adicionar na parte `client = Groq(api_key="SUA_CHAVE")` do código;


## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run .\src\teste_final.py
```
