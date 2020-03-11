from classParser import Parser
from dict import Dict
from classesWordRootType import Word, Root, Type, Epithet
import re

parser = Parser(Dict())
for i in range(1, 16):
    fileName = str(i) + '.txt'
    inFile = open(fileName, 'r', encoding = 'utf8').read()
    formula = parser.parse(inFile)
    print(i, inFile)
    print(formula.words)
    print(i, formula.getSchema())
    print(i, formula.formula)
    print(i, formula.isValid())
    print('\n')

