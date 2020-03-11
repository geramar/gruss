import re

class Word:
    def __init__(self, word, dicts):
        self.dicts = dicts
        self.word = word
        root = dicts.get_root(self.word)
        if root:
            self.root = Root(root, self.dicts)
        else:
            self.root = UnknownRoot(root, self.dicts)

    def getRoot(self):
        return self.root

    def getType(self):
        return self.getRoot().getType()

    def getNorma(self):
        norma = self.dicts.get_norma(self.word)
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
        return self.word


class Root:
    def __init__(self, root, dicts):
        self.dicts = dicts
        self.root = root
        type = self.dicts.get_type(self.root)
        if type:
            if str(type).isupper():
                self.type = Nomination(self.dicts.get_type(self.root), self.dicts)
            elif re.match('\w\d', str(type)):
                self.type = Epithet(self.dicts.get_type(self.root), self.dicts)
            else:
                self.type = Type(self.dicts.get_type(self.root), self.dicts)
        else:
            self.type = Type(self.dicts.get_type(self.root), self.dicts)


    def getType(self):
        return self.type

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
        return self.root


class UnknownRoot(Root):
    def getType(self):
        return UnknownType(None, self.dicts)

    def getWords(self):
        return set()

    def getTypeSynonyms(self):
        return set()

    def __repr__(self):
        return 'None'


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


class UnknownType(Type):
    def getRoots(self):
        return set()
    def __repr__(self):
        return '***'


class Nomination(Type):
    def __repr__(self):
        return self.type


class Epithet(Type):
    def get_nomination(self):
        return Nomination(self.type[0].upper(), self.dicts)
    def get_index(self):
        return int(self.type[-1])
