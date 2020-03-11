from classParser import Parser
from dict import Dict
from classesWordRootType import Word, Root, Type, Epithet

parser = Parser(Dict())
for i in range(1, 16):
    fileName = str(i) + '.txt'
    inFile = open(fileName, 'r', encoding = 'utf8').read()
    formula = parser.parse(inFile)
    print(i, inFile)
    print(i, formula.getSchema())
    print(i, formula.formula)
    for el in formula.formula:
        if isinstance(el, Epithet):
            print(el.get_index(), el.get_nomination())
    print(i, formula.isValid())
    print('\n')

