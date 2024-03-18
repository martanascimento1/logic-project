from sympy import symbols
from sympy.logic.boolalg import Or, And, Not
from sympy.logic.inference import satisfiable, valid
from sympy import simplify

# Definindo as variáveis lógicas
A, B, C = symbols('A B C')

# Criando a sentença lógica
sentenca = And(Or(A, B), Not(C))

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