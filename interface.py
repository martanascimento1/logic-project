from sympy import symbols
from sympy.logic.boolalg import And, Implies
from sympy.parsing.sympy_parser import parse_expr, ParseError

# Definindo as variáveis lógicas
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S = symbols('A B C D E F G H I J K L M N O P Q R S')

def modus_ponens(p, q, valor_p):
    if valor_p:
        return q
    else:
        return None

def seletor(funcao):
    if funcao == '1':
        sentenca = input('Digite a sentença em linguagem lógica: ')
        try:
            sentenca = parse_expr(sentenca)
            # Aqui você pode adicionar o código para simplificar a sentença
        except ParseError:
            print('Erro ao analisar a sentença. Por favor, tente novamente.')
    elif funcao == '2':
        sentenca = input('Digite a sentença em linguagem natural: ')
        # Aqui você pode adicionar o código para resolver a sentença
    else:
        print('função inválida!')
        funcao = input(str('Digite uma função válida: '))
        seletor(funcao)

print('FUNCAO 1 -> SIMPLIFICAR SENTENÇA EM LINGUAGEM LOGICA')
print('FUNCAO 2 -> RESOLUCAO DE SENTENÇA EM LINGUAGEM NATURAL')
funcao = input(str('Digite a função desejada: '))
seletor(funcao)
