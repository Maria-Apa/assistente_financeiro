def verificar_calculo(msg):
    msg_lower = msg.lower()

    palavras = ["calcule", "simule", "quanto rende", "%", "juros"]

    if any(w in msg_lower for w in palavras):
        return "Não faço simulações ou cálculos, mas posso te explicar como o conceito funciona 😊"

    return None
