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
from nltk.inference.resolution import ResolutionProver
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
        print('VOCÊ SELECIONOU INFORMAR A SENTENÇA NO FORMATO DE EXPRESSÃO LÓGICA')
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
        print('VOCÊ SELECIONOU INFORMAR A SENTENÇA NO FORMATO DE LINGUAGEM NATURAL')
        read_expr = Expression.fromstring

        """...................FORMATO DE ENTRADA PARA 2 PREMISSAS E UMA HIPÓTESE.................

        premissa 1 = (all x.(caracteristica(x) -> consequencia(x))))
        exemplo: (all x.(mulher(x) -> legal(x))) // (para toda pessoa, se a pessoa é mulher -> então a pessoa é legal)

        premissa 2 = (caracteristica(fulano))
        exemplo: (mulher(fulana)) // (fulana é mulher)

        hipótese = (consequencia(fulano))
        exemplo: (legal(fulana)) // (fulana é legal)"""

        p1 = read_expr(input(str('digite a primeira premissa: ')))
        p2 = read_expr(input(str('digite a segunda premissa: ')))
        c = read_expr(input(str('digite a hipotese: ')))
        logic.Counter._value = 0
        tp = ResolutionProver().prove(c, [p1,p2], verbose = True)
        tp.prove()

        print(tp.proof())
    else:
        print('função inválida!')
        funcao = input(str('Digite uma função válida: '))
        seletor(funcao)

print('FUNCAO 1 -> SIMPLIFICAR SENTENÇA EM LINGUAGEM LOGICA')
print('FUNCAO 2 -> RESOLUCAO DE SENTENÇA EM LINGUAGEM NATURAL')
funcao = input(str('Digite a função desejada: '))
seletor(funcao)