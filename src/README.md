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

- Crie uma pasta chamada "Lumi".
- Dentro dela, crie a pasta "data" e coloque todos os arquivos .json.
- Crie também a pasta "src" e coloque dentro dela o código do assistente (como app.py).
- No site groq.com, crie uma conta.
- Acesse o menu API Keys.
- Clique em "CREATE API KEY".
- Copie a chave gerada.
- No código, substitua a linha:
```
client = Groq(api_key="SUA_CHAVE")
```
pela chave que você copiou.
- No terminal, execute o comando para iniciar o Lumi:
```
streamlit run .\src\app.py
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run .\src\teste_final.py
```

## Evidência

<img width="1728" height="832" alt="image" src="https://github.com/user-attachments/assets/6242e2c7-ac6b-4cfe-b304-890a28056e60" />




