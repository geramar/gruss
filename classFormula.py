from classesWordRootType import Type, UnknownType

class Formula:
    def __init__(self, words, dicts):
        self.words = words
        self.dicts = dicts
        self.formula = list(map(lambda x: x.getType(), self.words))
        self.ordnung = list(
            map(
                lambda x: Type(x, self.dicts),
                ['h', 'H', 's2', 's3', 'S', 'r4', 'r5', 'H', 'R', 'R']
            )
        )

    def firstValid(self):
        value = False
        i = 0
        beginning = self.formula.index('h')
        for type in self.formula[::-1]:
            if not isinstance (type, UnknownType):
                ending = self.formula.index(type)
                break
        test = 1
        for type in self.formula:
            for el in range(i, len(self.ordnung)):
                if type == 'i' or type == self.ordnung[el]:
                    i = el + 1
                    test += 1
                    break

        if test == len(self.formula[beginning:ending + 1]):
            if beginning == 0 and ending == len(self.formula) - 1:
                value = 'Totally correct'
            elif beginning == 0:
                value = 'Correct until ' + str(ending + 1) + 'th word'
            elif ending == self.words[-1]:
                value = 'Correct starting from ' + str(beginning + 1)
            else:
                value = 'Correct starting from ' + str(beginning + 1) + 'th word ' + 'ending at ' + str(ending + 1) + 'th word'
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
