from classParser import Parser

class Formula:
    def __init__(self, data, parser=Parser()):
        self.parser = parser
        self.data = self.parser.parse(data)
    def getFormula(self):
        formula = list(map(lambda x: x.getType(), self.data))
        return '-'.join(map(str, formula))
    def __repr__(self):
        return str(self.data)
