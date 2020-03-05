from classParser import Parser
from dict import Dict

parser = Parser(Dict())
for i in range(1, 14):
    fileName = str(i) + '.txt'
    inFile = open(fileName, 'r', encoding = 'utf8').read()
    formula = parser.parse(inFile)
    print(i, inFile)
    print(i, formula.getSchema())
    print(i, formula.isValid())
    print('\n')
