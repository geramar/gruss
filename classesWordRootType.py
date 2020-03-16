import re


class Word:
    def __init__(self, word, dicts):
        self.dicts = dicts
        self.word = word
        root = self.dicts.get_root(self.word)
        if root:
            self.root = Root(root, self.dicts)
        else:
            self.root = UnknownRoot(root, self.dicts)

    def get_root(self):
        return self.root

    def get_type(self):
        return self.get_root().get_type()

    def get_norma(self):
        norma = self.dicts.get_norma(self.word)
        return Word(norma, self.dicts)

    def get_root_synonyms(self):
        all_synonyms = self.get_root().get_words()
        synonyms = set()
        for el in all_synonyms:
            if str(el) != str(self.get_norma()):
                synonyms.add(el)
        return synonyms

    def get_functional_synonyms(self):
        syn = set()
        for root in self.get_root().get_type_synonyms():
            syn |= root.get_words()
        return syn

    def __eq__(self, other):
        if isinstance(other, str):
            return self.word == other
        elif isinstance(other, self.__class__):
            return self.word == other.word
        else:
            return NotImplemented

    def __repr__(self):
        return self.word


class Root:
    def __init__(self, root, dicts):
        self.dicts = dicts
        self.root = root
        type = self.dicts.get_type(root)
        if type:
            if str(type).isupper():
                self.type = Nomination(self.dicts.get_type(self.root), self.dicts)
            elif re.match('\w\d', str(type)):
                self.type = Epithet(self.dicts.get_type(self.root), self.dicts)
            else:
                self.type = Type(self.dicts.get_type(self.root), self.dicts)
        else:
            self.type = UnknownType(self.dicts.get_type(self.root), self.dicts)

    def get_type(self):
        return self.type

    def get_words(self):
        return set(map(lambda w: Word(w, self.dicts), self.dicts.get_words(self.root)))

    def get_type_synonyms(self):
        all_synonyms = self.get_type().get_roots()
        synonyms = set()
        for el in all_synonyms:
            if str(el) != str(self):
                synonyms.add(el)
        return synonyms

    def __repr__(self):
        return self.root


class UnknownRoot(Root):
    def get_type(self):
        return UnknownType(None, self.dicts)

    def get_words(self):
        return set()

    def get_type_synonyms(self):
        return set()

    def __repr__(self):
        return 'None'


class Type:
    def __init__(self, type, dicts):
        self.type = type
        self.dicts = dicts

    def get_roots(self):
        return set(map(lambda r: Root(r, self.dicts), self.dicts.get_roots(self.type)))

    def get_words(self):
        words = set()
        roots = self.get_roots()
        for root in roots:
            words |= root.get_words()
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

    def get_correlation(self):
        return 'None'


class UnknownType(Type):
    def get_roots(self):
        return set()

    def __repr__(self):
        return '***'


class Nomination(Type):
    def __repr__(self):
        return self.type

    def get_correlation(self):
        epithets = set()
        for element in self.dicts.root_to_type:
            if self.dicts.root_to_type[element][0] == self.type.lower():
                epithets.add(self.dicts.root_to_type[element])
        epithets = list(map(lambda x: Type(x, self.dicts), epithets))
        return epithets


class Epithet(Type):
    def get_correlation(self):
        return Nomination(self.type[0].upper(), self.dicts)

    def get_index(self):
        return int(self.type[-1])
