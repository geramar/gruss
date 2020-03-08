from classesWordRootType import Type, UnknownType
from classValidator import Validator
import copy


class Formula:
    def __init__(self, words, dicts):
        self.words = words
        self.dicts = dicts
        self.formula = list(map(lambda x: x.getType(), self.words))
        self.schema = copy.deepcopy(self.formula)
        self.ordnung = list(
            map(
                lambda x: Type(x, self.dicts),
                ['h', 'H', 's2', 's3', 'S', 'r4', 'r5', 'H', 'R', 'R']
            )
        )

    def isValid(self):
        validation = Validator(self.ordnung, self.formula)
        return validation.validate()

    def getSchema(self):
        for element in self.schema:
            if element == 'R':
                i = self.schema.index(element)
                self.schema[i] = str(self.schema[i]) + str(self.words[i].getRoot())[0].upper()
        return '-'.join(map(str, self.schema))

    def __repr__(self):
        return str(self.words)
