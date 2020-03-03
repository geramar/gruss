from classFormula import Formula

fileName = str(input('Название файла: ')+ '.txt')
inFile = open(fileName, 'r', encoding = 'utf8').read()
data = Formula(inFile)
print(data.getFormula())
