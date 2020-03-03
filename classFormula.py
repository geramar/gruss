
class Formula:
    def __init__(self, words):
        self.words = words
    def getSchema(self):
        formula = list(map(lambda x: x.getType(), self.words))
        return '-'.join(map(str, formula))
    def __repr__(self):
        return str(self.words)
