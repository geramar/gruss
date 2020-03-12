from classesWordRootType import Word, Epithet
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

        i = -1
        for element in elements:
            i += 1

            if element == 'hoch' and elements[i] != elements[-1]:
                if isinstance(elements[i + 1].get_type(), Epithet):
                    elements[i + 1] = Word(str('hoch' + str(elements[i + 1])), self.dicts)
                    elements.pop(i)

            if element.get_type() == 'H' and elements[i] != elements[-1]:
                if elements[i + 1].get_type() == 'S' or elements[i + 1].get_type() == 'R':
                    elements[i + 1] = Word(str(elements[i]) + ' ' + str(elements[i + 1]), self.dicts)
                    elements.pop(i)

            if element.get_type() == 'und':
                i = elements.index(element)
                elements.pop(i)

        return Formula(elements, self.dicts)
