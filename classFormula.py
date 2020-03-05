from classesWordRootType import Type

class Formula:
    def __init__(self, words, dicts):
        self.words = words
        self.dicts = dicts
        self.ordnung = list(
            map(
                lambda x: Type(x, self.dicts),
                ['h', 'H', 's2', 's3', 'S', 'r4', 'r5', 'H', 'R']
            )
        )

    def isValid(self):
        value = False
        if self.words[0].getType() == 'h':
            i = 1
            test = [1]
            for type in list(map(lambda x: x.getType(), self.words[1:])):
                for el in range(i, len(self.ordnung)):
                    if type == 'i':
                        i = el
                        test.append(1)
                        break
                    if type == self.ordnung[el]:
                        i = el
                        test.append(1)
                        break
            if len(test) == len(self.words):
                value = True
        return value





    def getSchema(self):
        formula = list(map(lambda x: x.getType(), self.words))
        return '-'.join(map(str, formula))
    def __repr__(self):
        return str(self.words)
