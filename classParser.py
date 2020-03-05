from classesWordRootType import Word, Type
from classFormula import Formula
import re


class Parser:
    def __init__(self, dicts):
        self.dicts = dicts
    def parse(self, data):
        elements = list(
            map(
                lambda x: Word(x, self.dicts),
                re.sub('[^a-zA-Zäüöß\s]', '', data).lower().split()
            )
        )

        for element in elements:
            if element.getType() == 'H':
                i = elements.index(element)
                if elements[i] == elements[-1]:
                    continue
                elif elements[i + 1].getType() == 'S' or elements[i + 1].getType() == 'R':
                    elements[i + 1] = Word(str(elements[i]) + ' ' + str(elements[i + 1]), self.dicts)
                    elements.pop(i)
            if element.getType() == 'und':
                i = elements.index(element)
                elements.pop(i)

        return Formula(elements, self.dicts)
