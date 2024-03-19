from nltk.sem import logic
from nltk.ccg import logic
from nltk.inference import resolution
from nltk.inference import discourse
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