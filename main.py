from classFormula import Formula

for i in range(1, 5):
    fileName = str(i) + '.txt'
    #fileName = str(input('Название файла: ')+ '.txt')
    inFile = open(fileName, 'r', encoding = 'utf8').read()
    data = Formula(inFile)
    print(i, data.getFormula())
