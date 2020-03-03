from classFormula import Formula

parser = Parser(Dict())
for i in range(1, 5):
    fileName = str(i) + '.txt'
    inFile = open(fileName, 'r', encoding = 'utf8').read()
    formula = parser.parse(inFile)
    print(i, formula.getSchema())
