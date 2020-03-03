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
            'und' : 'und',
            'unknown' : 'unknown'
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
            'insonders' : 'insonderst',
            'herr professor': 'professor',
            'herr vatter': 'vater',
            'herr gönner': 'gönner',
            'herr vater': 'vater',
            'herr freund': 'freund',
        }

    def get_root(self, word):
        if word in self.analogs:
            word = self.analogs[word]
        if word in self.word_to_root:
            root = self.word_to_root[word]
        else:
            root = 'unknown'
        return root

    def get_type(self, root):
        if root in self.root_to_type:
            type = self.root_to_type[root]
        else:
            type = 'unknown'
        return type

    def get_roots(self, type):
        roots = set()
        for root in self.root_to_type:
            if self.root_to_type[root] == type:
                roots.add(root)
        return roots

    def get_words(self, root):
        words = set()
        for word in self.word_to_root:
            if self.word_to_root[word] == root:
                words.add(word)
        return words
