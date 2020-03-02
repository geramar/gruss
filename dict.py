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

    def get_type(self, root):
        if root in self.root_to_type:
            self.type = self.root_to_type[root]
            return self.type

    def get_roots(self, type):
        self.roots = set()
        for root in self.root_to_type:
            if self.root_to_type[root] == type:
                self.roots.add(root)
        return self.roots


    def get_words(self, root):
        self.words = set()
        if root in self.root_to_set:
            self.words = self.root_to_set[root]
        return self.words

dicts = Dict()
#a = str(input())
#print(dicts.get_root(a))
