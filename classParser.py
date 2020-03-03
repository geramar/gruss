from classesWordRootType import Word, Type
from classFormula import Formula
import re


class Parser:
    def __init__(self, dict):
        self.dict = dict
    def parse(self, data):
        elements = list(
            map(
                lambda x: Word(x, self.dict),
                re.sub('[^a-zA-Zäüöß\s]', '', data).lower().split()
            )
        )

        for element in elements:
            if str(element.getType()) == 'H':
                i = elements.index(element)
                if str(elements[i + 1].getType()) == 'S' or str(elements[i + 1].getType()) == 'R':
                    elements[i + 1] = Word(str(elements[i]) + ' ' + str(elements[i + 1]), self.dict)
                    elements.pop(i)
            if str(element.getType()) == 'und':
                i = elements.index(element)
                elements.pop(i)

        return Formula(elements)
