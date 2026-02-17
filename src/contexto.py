import json
from utils.loader import load_json

produtos = load_json("produtos_financeiros.json")
info = load_json("info_financeira.json")
riscos = load_json("riscos_financeiros.json")
tributos = load_json("tributacao_financeira.json")
perfil = load_json("perfil_investidor.json")

def montar_contexto(msg):
    contexto = []
    msg_lower = msg.lower()

    if any(p in msg_lower for p in ["perfil", "conservador", "moderado", "arrojado"]):
        contexto.append("PERFIL DO INVESTIDOR:\n" + json.dumps(perfil, indent=2, ensure_ascii=False))

    if any(p in msg_lower for p in ["invest", "cdb", "tesouro", "fundo", "lci", "lca"]):
        contexto.append("PRODUTOS FINANCEIROS:\n" + json.dumps(produtos, indent=2, ensure_ascii=False))

    if "risco" in msg_lower:
        contexto.append("RISCOS FINANCEIROS:\n" + json.dumps(riscos, indent=2, ensure_ascii=False))

    if "imposto" in msg_lower or "ir" in msg_lower or "tribut" in msg_lower:
        contexto.append("TRIBUTAÇÃO:\n" + json.dumps(tributos, indent=2, ensure_ascii=False))

    if any(x in msg_lower for x in ["o que é", "como funciona", "explica", "defina"]):
        contexto.append("INFORMAÇÕES FINANCEIRAS:\n" + json.dumps(info, indent=2, ensure_ascii=False))

    return "\n\n".join(contexto)

    if any(q in msg for q in ["o que é", "como funciona", "explique", "defina"]):
        bloco.append("INFO:\n" + json.dumps(info, indent=2, ensure_ascii=False))

    return "\n\n".join(bloco)
