import json
from utils.loader import load_json

produtos = load_json("produtos_financeiros.json")
perfil = load_json("perfil_investidor.json")
riscos = load_json("riscos_financeiros.json")
info = load_json("info_financeira.json")
tributacao = load_json("tributacao_financeira.json")

def montar_contexto(msg):
    msg = msg.lower()
    bloco = []

    if any(p in msg for p in ["cdb", "tesouro", "lci", "lca", "investimento"]):
        bloco.append("PRODUTOS:\n" + json.dumps(produtos, indent=2, ensure_ascii=False))

    if "perfil" in msg:
        bloco.append("PERFIL DO INVESTIDOR:\n" + json.dumps(perfil, indent=2, ensure_ascii=False))

    if "risco" in msg:
        bloco.append("RISCOS:\n" + json.dumps(riscos, indent=2, ensure_ascii=False))

    if "imposto" in msg or "tribut" in msg:
        bloco.append("TRIBUTAÇÃO:\n" + json.dumps(tributacao, indent=2, ensure_ascii=False))

    if any(q in msg for q in ["o que é", "como funciona", "explique", "defina"]):
        bloco.append("INFO:\n" + json.dumps(info, indent=2, ensure_ascii=False))

    return "\n\n".join(bloco)
