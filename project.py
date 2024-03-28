def modus_ponens(premissas, conclusao):
    if "P -> Q" in premissas and "P" in premissas:
        return True
    return False

def modus_tollens(premissas, conclusao):
    if "P -> Q" in premissas and "/Q" in premissas:
        return True
    return False

def silogismo_hipotetico(premissas, conclusao):
    if "A -> B" in premissas and "B -> C" in premissas:
        return True
    return False

def silogismo_disjuntivo(premissas, conclusao):
    if "P * Q" in premissas and "/P" in premissas:
        return True
    return False

def operacoes_logicas(premissas, conclusao):
    if "P & Q" in premissas and "P" in premissas:
        if "Q" in premissas:
            return True
        return False
    elif "P & Q" in premissas and "Q" in premissas:
        if "P" in premissas:
            return True
        return False

"""FORMATO DE ENTRADA EX.: 
PREMISSA = ["A -> B", "B -> C", "A"]
CONCLUSÃO  = "C" """

premissas_exemplo = input('Digite as premissas (usando letras de A a Z): ')
conclusao_exemplo = input("Digite a conclusão (usando letras de A a Z): ")

regras = [modus_ponens, modus_tollens, silogismo_hipotetico, silogismo_disjuntivo]

valido = False
for regra in regras:
    resultado = regra(premissas_exemplo, conclusao_exemplo)
    if resultado:
        valido = True
        break

if valido:
    print("O argumento é válido.")
else:
    print("O argumento é inválido.")
