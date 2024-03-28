def modus_ponens(premissas, conclusao):
    if "P -> Q" in premissas and "P" in premissas and conclusao == "Q":
        return True
    return False

def modus_tollens(premissas, conclusao):
    if "P -> Q" in premissas and "/Q" in premissas and conclusao == "/P":
        return True
    return False

def silogismo_hipotetico(premissas, conclusao):
    if "A -> B" in premissas and "B -> C" in premissas and conclusao == "A -> C":
        return True
    return False

def silogismo_disjuntivo(premissas, conclusao):
    if "P * Q" in premissas and "/P" in premissas and conclusao == "Q":
        return True
    return False

def operacoes_logicas(premissas, conclusao):
    if "P & Q" in premissas and "P" in premissas and conclusao == "Q":
        return True
    elif "P & Q" in premissas and "Q" in premissas and conclusao == "P":
        return True
    return False