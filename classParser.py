from classesWordRootType import Word
import re
import copy

class Parser:
    def __init__(self, data):
        self.matrix = [[],[]]
    def parse(self, data):
        self.text = list(
            map(
                lambda x: Word(x),
                re.sub('[^a-zA-Zäüöß\s]', '', data).lower().split()
            )
        )

        self.formul = list(
            map(
                lambda x: x.getType(), self.text
            )
        )
        for word in self.text:
            if word.type == 'H':
                i = self.text.index(word)
                if self.text[i + 1].type == 'S' or self.text[i + 1].type == 'R':
                    self.text[i + 1] = str(self.text[i]) + ' ' + str(self.text[i + 1])
                    self.text.pop(i)
                    self.formul.pop(i)
            if word.type == 'und':
                i = self.text.index(word)
                self.text.pop(i)
                self.formul.pop(i)
        self.matrix[0] = self.text
        self.matrix[1] = self.formul
        return self.matrix
    def __repr__(self):
        return str(self.matrix)
