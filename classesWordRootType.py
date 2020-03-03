

class Word:
    def __init__(self, word, dicts):
        self.dicts = dicts
        self.word = word
        self.root = Root(self.dicts.get_root(self.word), self.dicts)

    def getRoot(self):
        return self.root

    def getType(self):
        return self.getRoot().getType()

    def getNorma(self):
        norma = self.word
        if self.word in self.dicts.analogs:
            norma = self.dicts.getNorma(self.word)
        return Word(norma, self.dicts)

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
    def __init__(self, root, dicts):
        self.dicts = dicts
        self.root = root
        self.type = Type(self.dicts.get_type(self.root), self.dicts)

    def getType(self):
        self.type

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
    def __init__(self, type, dicts):
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
        return self.type

    def __eq__(self, other):
        if isinstance(other, str):
            return self.type == other
        elif isinstance(other, self.__class__):
            return self.type == other.type
        else:
            return NotImplemented
