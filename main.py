from classParser import Parser
from dict import Dict
from classValidator import Validator


parser = Parser(Dict())
for i in range(1, 16):
    fileName = str(i) + '.txt'
    inFile = open(fileName, 'r', encoding='utf8').read()
    formula = parser.parse(inFile)
    print(i,inFile)
    print(formula.words)
    print(i, formula.get_schema())
    print(i, formula.formula)
    print(i, formula.is_valid())
    print(i, formula.get_value())
    print('\n')
