from classParser import Parser

class Formula:
    def __init__(self, data = ):
        parser = Parser()
        self.data = parser.parse(data)
    def __repr__(self):
        return str(self.data)

fileName = str(input('Название файла: ')) + '.txt'
print("Meow")
fileData = open(fileName, 'r', encoding = 'utf8').read()
print(fileData)

print(Formula(fileData))
#formula = Formula(parser)

