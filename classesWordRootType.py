from dict import Dict


class Word:
    def __init__(self, word, dicts=Dict()):
        self.dicts = dicts
        self.word = word

    def getRoot(self):
        return Root(self.dicts.get_root(self.word), dicts = self.dicts)

    def getType(self):
        return self.getRoot().getType()

    def getNorma(self):
        norma = self.word
        if self.word in self.dicts.analogs:
            norma = self.dicts.analogs[self.word]
        return Word(norma)

    def getRootSynonyms(self):
        allSynonyms = self.getRoot().getWords()
        synonyms = set()
        for el in allSynonyms:
            if str(el) != str(self.getNorma()):
                synonyms.add(el)
        return synonyms

    def getFunctionalSynonyms(self):
        syn = set()
        for root in self.getRoot().getTypeSynonyms():
            syn |= root.getWords()
        return syn

    def __repr__(self):
        return str(self.word)

class Root:
    def __init__(self, root, dicts=Dict()):
        self.dicts = dicts
        self.root = root

    def getType(self):
        return Type(self.dicts.get_type(self.root), dicts = self.dicts)

    def getWords(self):
        return set(map(lambda w: Word(w, self.dicts), self.dicts.get_words(self.root)))

    def getTypeSynonyms(self):
        allSynonyms = self.getType().getRoots()
        synonyms = set()
        for el in allSynonyms:
            if str(el) != str(self):
                synonyms.add(el)
        return synonyms

    def __repr__(self):
        return str(self.root)

class Type:
    def __init__(self, type, dicts=Dict()):
        self.type = type
        self.dicts = dicts

    def getRoots(self):
        return set(map(lambda r: Root(r, self.dicts), self.dicts.get_roots(self.type)))

    def getWords(self):
        words = set()
        roots = self.getRoots()
        for root in roots:
            words |= root.getWords()
        return words

    def __repr__(self):
        return str(self.type)

w = input()
a = Word(w)
print('1. ', a)
b = a.getRoot()
print('2. ', b)
c = a.getType()
print('3. ', c)
print('4. ', b.getType())
d = b.getWords()
print('5. ', d)
e = list(d)
print('6. ', e)
f = e[0]
print('7. ', f)
print('8. ', f.getRoot())
print('9. ', f.getType())
g = c.getRoots()
print('10. ', g)
h = c.getWords()
print('11. ', h)
i = list(g)
j = i[0]
print(j)
print('12. ', j.getWords())
print('13. ', j.getType())
k = list(h)
l = k[0]
print(l)
print('14. ', l.getRoot())
print('15. ', l.getType())
print('16. ', a.getRootSynonyms())
print('17. ', a.getNorma())
print('18. ', b.getTypeSynonyms())
print('19. ', a.getFunctionalSynonyms())