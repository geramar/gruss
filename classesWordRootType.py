from dict import Dict

class Word:
    def __init__(self, word, root = '', type = '', synonyms = set()):
        dicts = Dict()
        self.word = word
        self.root = dicts.get_root(self.word)
        self.type = dicts.get_type(self.word)
        self.synonyms = dicts.get_synonyms(self.word)
    def __repr__(self):
        return str(self.word)

class Root:
    def __init__(self, root, words = set(), type = ''):
        dicts = Dict()
        self.root = root
        self.words = dicts.rget_words_from_root(self.root)
        self.type = dicts.get_type_from_root(self.root)
    def __repr__(self):
        return str(self.root)

class Type:
    def __init__(self, type, roots = set(), words = set()):
        dicts = Dict()
        self.type = type
        self.roots = dicts.rget_roots(self.type)
        self.words = dicts.rget_words(self.type)
    def __repr__(self):
        return str(self.type)
