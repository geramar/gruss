import copy

class Dict:
    def __init__(self):
        self.word_to_root = {
            'hochwohlgeborner' : 'wohlgeb',
            'wohlgeborner' : 'wohlgeb',
            'hochedelgeborner' : 'edelgeb',
            'hochgelehrter' : 'lehr',
            'hochgelehrtester' : 'lehr',
            'hochzuehrender' : 'ehr',
            'hochgeehrter' : 'ehr',
            'hochgeehrtester' : 'ehr',
            'hochgeneigter' : 'geneig',
            'geneigter' : 'geneig',
            'hochgeneigtester' : 'geneig',
            'geneigtester' : 'geneig',
            'gnädiger' : 'gnädig',
            'gnädigster': 'gnädig',
            'gütiger' : 'gütig',
            'gütigster': 'gütig',
            'hochzuschätzender' : 'schätz',
            'hochgeschätzter' : 'schätz',
            'hochgeschätztester': 'schätz',
            'professor' : 'Stelle',
            'herr' : 'herr',
            'gönner' : 'gönner',
            'vater' : 'vater',
            'freund' : 'freund',
            'insonderst' : 'insond',
            'und' : 'und'
        }

        self.root_to_type = {
            'wohlgeb' : 'h',
            'edelgeb' : 'h',
            'lehr' : 's2',
            'ehr' : 's3',
            'geneig' : 'r4',
            'gnädig' : 'r4',
            'gütig' : 'r4',
            'schätz' : 'r5',
            'Stelle' : 'S',
            'herr' : 'H',
            'gönner' : 'R',
            'vater' : 'R',
            'freund' : 'R',
            'insond' : 'i',
            'und' : 'und'
        }

        self.root_to_set = {
            'wohlgeb' : {'Hochwohlgeborner', 'Wohlgeborner'},
            'edelgeb' : {'HochEdelgeborner'},
            'lehr' : {'Hochgelehrter', 'Hochgelehrtester'},
            'ehr' : {'Hochzuehrender', 'Hochgeehrter', 'Hochgeehrtester'},
            'geneig' : {'Hochgeneigter', 'Geneigter', 'Hochgeneigtester', 'Geneigtester'},
            'gütig' : {'Gütiger', 'Gütigster'},
            'schätz' : {'Hochzuschätzender', 'Hochgeschätzter'},
            'Stelle': {'Professor'},
            'herr': {'Herr'},
            'gönner': {'Gönner'},
            'vater': {'Vater'},
            'freund': {'Freund'}
        }

        self.analogs = {
            'wolgeborner' : 'wohlgeborner',
            'hochwolgeborner' : 'hochwohlgeborner',
            'hochgelahrter' : 'hochgelehrter',
            'hochgelährter' : 'hochgelehrter',
            'hochgelahrtester' : 'hochgelehrtester',
            'hochgelährtester' : 'hochgelehrtester',
            'hochgelarter': 'hochgelehrter',
            'hochgelärter': 'hochgelehrter',
            'hochgelartester': 'hochgelehrtester',
            'hochgelärtester': 'hochgelehrtester',
            'hochgelerter': 'hochgelehrter',
            'hochgelertester': 'hochgelehrtester',
            'vatter' : 'vater',
            'insonders' : 'insonderst'
        }

    def get_root(self, word):
        if word in self.analogs:
            word = self.analogs[word]
        if word in self.word_to_root:
            self.root = self.word_to_root[word]
            return self.root

    def get_type(self, word):
        self.get_root(word)
        if self.root in self.root_to_type:
            self.type = self.root_to_type[self.root]
            return self.type

    def get_type_from_root(self, root):
        if root in self.root_to_type:
            self.type = self.root_to_type[root]
            return self.type

    def rget_roots(self, type):
        self.roots = set()
        for root in self.root_to_type:
            if self.root_to_type[root] == type:
                self.roots.add(root)
        return self.roots

    def rget_words_from_root(self, root):
        self.words = set()
        if root in self.root_to_set:
            self.words = self.root_to_set[root]
        return self.words
    
    def rget_words(self, type):
        self.rget_roots(type)
        self.set_of_all_words = set()
        for root in self.roots:
            self.rget_words_from_root(root)
            self.set_of_all_words |= self.words
        return self.set_of_all_words

    def get_synonyms(self, word):
        if word in self.analogs:
            word = self.analogs[word]
        self.synonyms = [set(), set()]
        self.get_type(word)
        self.rget_roots(self.type)
        for root in self.roots:
            self.rget_words_from_root(root)
            if root == self.root:
                self.synonyms[0] = copy.deepcopy(self.words)
                for synonym in self.words:
                    if synonym.lower() == word:
                        self.synonyms[0].remove(synonym)
            else:
                self.synonyms[1] |= self.words
        return self.synonyms

dicts = Dict()
#a = str(input())
#print(dicts.get_synonyms(a))




