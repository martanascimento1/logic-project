from sympy import symbols
from sympy.logic.boolalg import Or, And, Not
from sympy.logic.inference import satisfiable, valid
from sympy import simplify
from nltk.inference import discourse
from nltk.sem import logic
from nltk.ccg import logic
from nltk.inference import resolution
import operator
from collections import defaultdict
from functools import reduce
from nltk.inference import ResolutionProverCommand
from nltk.inference.api import BaseProverCommand, Prover
from nltk.inference import resolution
from nltk.sem import skolemize
from nltk.sem.logic import (
    AndExpression,
    ApplicationExpression,
    EqualityExpression,
    Expression,
    IndividualVariableExpression,
    NegatedExpression,
    OrExpression,
    Variable,
    VariableExpression,
    is_indvar,
    unique_variable,
)

def seletor(funcao):
    if funcao == '1':
        # Definindo as variáveis lógicas
        A, B, C = symbols('A B C')

        # Criando a sentença lógica
        sentenca = str(input("digite sua sentenca no formato: operacao(elemento1, elemento2): "))

        # Simplificando a sentença lógica
        sentenca_simplificada = simplify(sentenca)

        # Verificando se a sentença lógica é satisfatível
        resultado_satisfativel = satisfiable(sentenca_simplificada)

        # Verificando se a sentença lógica é uma tautologia
        resultado_tautologia = valid(sentenca_simplificada)

        # Verificando se a sentença lógica é uma contradição
        resultado_contradição = not resultado_satisfativel and not resultado_tautologia

        print(f'Sentença simplificada: {sentenca_simplificada}')
        print(f'Satisfatível: {resultado_satisfativel}')
        print(f'Tautologia: {resultado_tautologia}')
        print(f'Contradição: {resultado_contradição}')
    
    elif funcao == '2':
        read_expr = Expression.fromstring

        """p1 = read_expr('all x.(man(x) -> mortal(x))')
        p2 = read_expr('man(Socrates)')
        c = read_expr('mortal(Socrates)')"""

        p1 = read_expr(input(str('digite a primeira premissa: ')))
        p2 = read_expr(input(str('digite a segunda premissa: ')))
        c = read_expr(input(str('digite a hipotese: ')))
        logic.Counter._value = 0
        tp = ResolutionProverCommand(c, [p1,p2])
        tp.prove()

        print(tp.proof())
    else:
        print('função inválida!')

print('funcao 1 -> sentença na linguagem logica')
print('funcao 2 -> sentença em linguagem natural')
funcao = input(str('Digite a função desejada: '))
seletor(funcao)