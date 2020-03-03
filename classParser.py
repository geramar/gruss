from classesWordRootType import Word, Type
import re


class Parser:
    def __init__(self):
        self.elements = []
    def parse(self, data):
        self.elements = list(
            map(
                lambda x: Word(x),
                re.sub('[^a-zA-Zäüöß\s]', '', data).lower().split()
            )
        )

        for element in self.elements:
            if str(element.getType()) == 'H':
                i = self.elements.index(element)
                if str(self.elements[i + 1].getType()) == 'S' or str(self.elements[i + 1].getType()) == 'R':
                    self.elements[i + 1] = Word(str(self.elements[i]) + ' ' + str(self.elements[i + 1]))
                    self.elements.pop(i)
            if str(element.getType()) == 'und':
                i = self.elements.index(element)
                self.elements.pop(i)
        return self.elements

    def __repr__(self):
        return str(self.elements)
