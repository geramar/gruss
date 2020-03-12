from classesWordRootType import Type, UnknownType


class Validator:
    def __init__(self, ordnung, formula):
        self.ordnung = ordnung
        self.formula = formula
        self.beginning = 0
        self.ending = len(self.formula)
        self.value = self.validate()

    def validate(self):
        self.value = 0
        for el in self.formula:
            if el == 'h1':
                self.beginning = self.formula.index('h1')
                break

        i_end = len(self.formula)

        for el in self.formula[::-1]:
            i_end -= 1
            if not isinstance(el, UnknownType):
                 break
        self.ending = i_end

        i = 0
        test = 0
        for type in self.formula[self.beginning:]:
            for el in range(i, len(self.ordnung)):
                if type == 'i' or type == self.ordnung[el]:
                    i = el + 1
                    test += 1
                    break
        if test == len(self.formula[self.beginning:self.ending]):
            if self.beginning == 0 and self.ending == len(self.formula) - 1:
                self.value = 1
            elif self.beginning == 0:
                self.value = (1, 0)
            elif self.ending == self.formula[-1]:
                self.value = (0, 1)
            else:
                self.value = (0, 0)

        if not self.value and all(list(map(lambda x: not isinstance(x, UnknownType), self.formula[self.beginning:self.ending + 1]))):
                self.value = -1

        return self.value
    
    def __repr__(self):
        if self.value == 1:
            return 'Totally correct'
        elif self.value == (1, 0):
            return 'Correct until ' + str(self.ending + 1) + 'th word'
        elif self.value == (0, 1):
            return 'Correct starting from ' + str(self.beginning + 1)
        elif self.value == (0, 0):
            return 'Correct starting from ' + str(self.beginning + 1) + 'th word ' + 'ending at ' + str(
                self.ending + 1) + 'th word'
        elif self.value == -1:
            return 'illineal'
        else:
            return 'not correct'
