from classParser import Parser
from dict import Dict
from classesWordRootType import Word, Root
from classValidator import Validator
import re

parser = Parser(Dict())
for i in range(1, 16):
    fileName = str(i) + '.txt'
    inFile = open(fileName, 'r', encoding='utf8').read()
    formula = parser.parse(inFile)
    print(i,inFile)
    print(formula.words)
    print(i, formula.get_schema())
    print(i, formula.types)
    print(i, formula.is_valid())
    print(i, formula.get_value())
    print(formula.words[1], formula.words[1].get_type())
    print(formula.words[1].get_type().get_correlation())
    print(formula.words[-1], formula.words[-1].get_type())
    print(formula.words[-1].get_type().get_correlation())
    print('\n')




