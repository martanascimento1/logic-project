def modus_ponens(premissas, conclusao):
    premissa1 = next((p for p in premissas if "->" in p), None)
    if premissa1 is None:
        return False

    premissa2 = next((p for p in premissas if p == premissa1.split(" -> ")[0]), None)

    if premissa1 and premissa2 and conclusao == premissa1.split(" -> ")[1]:
        return True
    return False

def modus_tollens(premissas, conclusao):
    premissa1 = next((p for p in premissas if "->" in p), None)
    if premissa1 is None:
        return False

    premissa2 = next((p for p in premissas if "->" in p and "/" + p.split(" -> ")[1] == premissa1), None)

    if premissa1 and premissa2 and conclusao == "/" + premissa1.split(" -> ")[0]:
        return True
    return False

def silogismo_hipotetico(premissas, conclusao):
    if "->" not in conclusao:
        return False

    conclusao_operando1, conclusao_operando2 = conclusao.split(" -> ")

    for p in premissas:
        if "->" in p:
            operando1, operando2 = p.split(" -> ")
            for q in premissas:
                if q != p and "->" in q:
                    operando3, operando4 = q.split(" -> ")
                    if operando1 == conclusao_operando1 and operando4 == conclusao_operando2 and operando2 == operando3:
                        return True
    return False

def silogismo_disjuntivo(premissas, conclusao):
    premissa1 = next((p for p in premissas if "*" in p), None)
    if premissa1 is None:
        return False

    premissa2 = next((p for p in premissas if "/" + p == premissa1.split(" * ")[0]), None)

    if premissa1 and premissa2 and conclusao == premissa1.split(" * ")[1]:
        return True
    return False

def operacoes_logicas(premissas, conclusao):
    premissa_com_and = next((p for p in premissas if "&" in p), None)
    if premissa_com_and is None:
        return False

    operando1, operando2 = premissa_com_and.split(" & ")

    if (operando1 == conclusao and operando2 in premissas) or (operando2 == conclusao and operando1 in premissas):
        return True

    return False


"""FORMATOS DE ENTRADA E SAÍDA ESPERADOS: 
MODUS PONENS
premissas = P -> Q, P
conclusao = Q

MODUS TOLLENS
premissas = P -> Q, /Q
conclusao = "/P

SILOGISMO HIPOTÉTICO: 
premissas = P -> Q, Q -> R
conclusao = P -> R

SILOGISMO DISJUNTIVO:
premissas = P * Q, /P
conclusao = Q

OPERAÇÕES LÓGICAS: 
premissas = P & Q, P
conclusao = Q
"""

premissas_exemplo = input('Digite as premissas (usando letras de A a Z): ')
premissas_exemplo = premissas_exemplo.split(', ')
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
