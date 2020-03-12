from classesWordRootType import Type, UnknownType


class Validator:
    def __init__(self, ordnung, formula):
        self.ordnung = ordnung
        self.formula = formula

    def validate(self):
        value = False
        beginning = 0

        for el in self.formula:
            if el == 'h1':
                beginning = self.formula.index('h1')
                break

        i_end = len(self.formula)

        for el in self.formula[::-1]:
            i_end -= 1
            if not isinstance(el, UnknownType):
                 break
        ending = i_end

        i = 0
        test = 0
        for type in self.formula[beginning:]:
            for el in range(i, len(self.ordnung)):
                if type == 'i' or type == self.ordnung[el]:
                    i = el + 1
                    test += 1
                    break
        if test == len(self.formula[beginning:ending]):
            if beginning == 0 and ending == len(self.formula) - 1:
                value = 'Totally correct'
            elif beginning == 0:
                value = 'Correct until ' + str(ending + 1) + 'th word'
            elif ending == self.formula[-1]:
                value = 'Correct starting from ' + str(beginning + 1)
            else:
                value = 'Correct starting from ' + str(beginning + 1) + 'th word ' + 'ending at ' + str(
                    ending + 1) + 'th word'

        if not value:
            print(self.formula[beginning:ending + 1])
            print(all(list(map(lambda x: not isinstance(x, UnknownType), self.formula[beginning:ending + 1]))))
            if all(list(map(lambda x: not isinstance(x, UnknownType), self.formula[beginning:ending + 1]))):
                print('AHAHA')

        return value
