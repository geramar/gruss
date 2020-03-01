from dict import Dict

class Word:
    def __init__(self, dicts, word):
        self.dicts = dicts
        self.word = word
    def getRoot(self):
        return Root(self.dicts, self.dicts.get_root(self.word))
    def getType(self):
        return self.getRoot().getType()
    def getSynonyms():
        words = self.getRoot().getWords()
        #... exclude word
        return words
    def getOtherSynonyms():
        ret = []
        for root in self.getRoot.getSynonyms():
            ret+= root.getWords()
        return ret 
    def __repr__(self):
        return str(self.word)

class Root:
    def __init__(self, dicts, root):
        self.dicts = dicts
        self.root = root
    def getType(self):
        return Type(self.dicts, dicts.get_type_from_root(self.root))
    def getSynonyms():
        roots = self.getType().getRoots()
        #... exclude root
        return roots
    def getWords(self):
        list(map(lambda w: Word(self, dicts, w), dicts.get_words_from_root(self.root)))
    def __repr__(self):
        return str(self.root)

class Type:
    def __init__(self, dicts, type):
        dicts = Dict()
        self.type = type
        self.roots = dicts.rget_roots(self.type)
        self.words = dicts.rget_words(self.type)
    def __repr__(self):
        return str(self.type)

w = Word('Meow', root='M')
r = w.getRoot()
