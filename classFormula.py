from classesWordRootType import Type

class Formula:
    def __init__(self, words, dicts):
        self.words = words
        self.dicts = dicts
        self.formula = list(map(lambda x: x.getType(), self.words))
        self.ordnung = list(
            map(
                lambda x: Type(x, self.dicts),
                ['h', 'H', 's2', 's3', 'S', 'r4', 'r5', 'H', 'R']
            )
        )

    def firstValid(self):
        value = False
        i = 0
        beginning = self.formula.index('h')
        test = [1]
        for type in self.formula:
            for el in range(i, len(self.ordnung)):
                if type == 'i':
                    i = el
                    test.append(1)
                    break
                if type == self.ordnung[el]:
                    i = el
                    test.append(1)
                    break
        if len(test) == len(self.words[beginning:]):
            value = True
        return value

    def isValid(self):
        if self.formula[0] == 'h':
            return self.firstValid()
        if self.formula[0] != 'h':
            for word in self.words:
                if word.getType() == 'h':
                    return self.firstValid()

    def getSchema(self):
        for element in self.formula:
            if element == 'R':
                i = self.formula.index(element)
                self.formula[i] = str(self.formula[i]) + str(self.words[i].getRoot())[0].upper()
        return '-'.join(map(str, self.formula))
    def __repr__(self):
        return str(self.words)
