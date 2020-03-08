from classesWordRootType import UnknownType


class Validator:
    def __init__(self, ordnung, formula):
        self.ordnung = ordnung
        self.formula = formula

    def validate(self):
        for word in self.formula:
            if word == 'h':
                value = False
                beginning = self.formula.index('h')
                i_end = len(self.formula)

                for type in self.formula[::-1]:
                    i_end -= 1
                    if not isinstance(type, UnknownType):
                        break
                ending = i_end

                i = 0
                test = 0
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
                    elif ending == self.formula[-1]:
                        value = 'Correct starting from ' + str(beginning + 1)
                    else:
                        value = 'Correct starting from ' + str(beginning + 1) + 'th word ' + 'ending at ' + str(
                            ending + 1) + 'th word'
                return value
