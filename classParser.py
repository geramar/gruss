from classesWordRootType import Word, Type
import re


class Parser:
    def __init__(self, data):
        self.elements = []
        self.data = data
    def parse(self):
        self.elements = list(
            map(
                lambda x: Word(x),
                re.sub('[^a-zA-Zäüöß\s]', '', self.data).lower().split()
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

inFile = open(str(input('Название файла: ')+ '.txt'), 'r', encoding = 'utf8').read()
data = Parser(inFile)
print(data.parse())
print(list(map(lambda x: x.getType(), data.parse())))