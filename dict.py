class Dict:
    def __init__(self):
        self.word_to_root = {
            'hochwohlgeborner': 'wohlgeb',
            'wohlgeborner': 'wohlgeb',
            'hochedelgeborner': 'edelgeb',
            'hochgelehrter': 'lehr',
            'hochgelehrtester': 'lehr',
            'hochzuehrender': 'ehr',
            'hochgeehrter': 'ehr',
            'hochgeehrtester': 'ehr',
            'hochgeneigter': 'geneig',
            'geneigter': 'geneig',
            'hochgeneigtester': 'geneig',
            'geneigtester': 'geneig',
            'gnädiger': 'gnädig',
            'gnädigster': 'gnädig',
            'gütiger': 'gütig',
            'gütigster': 'gütig',
            'hochzuschätzender': 'schätz',
            'hochgeschätzter': 'schätz',
            'hochgeschätztester': 'schätz',
            'professor': 'Stelle',
            'cammerherr': 'Stelle',
            'hofrath': 'Stelle',
            'bibliothecarius': 'Stelle',
            'herr': 'herr',
            'gönner': 'gönner',
            'vater': 'vater',
            'freund': 'freund',
            'insonderst': 'insond',
            'und': 'und'
        }

        self.root_to_type = {
            'wohlgeb': 'h1',
            'edelgeb': 'h1',
            'lehr': 's2',
            'ehr': 's3',
            'geneig': 'r4',
            'gnädig': 'r4',
            'gütig': 'r4',
            'schätz': 'r5',
            'Stelle': 'S',
            'herr': 'H',
            'gönner': 'R',
            'vater': 'R',
            'freund': 'R',
            'insond': 'i',
            'und': 'und'
        }

        self.analogs = {
            'wolgeborner': 'wohlgeborner',
            'hochwolgeborner': 'hochwohlgeborner',
            'wolgebohrner': 'wohlgeborner',
            'hochwolgebohrner': 'hochwohlgeborner',
            'wohlgebohrner': 'wohlgeborner',
            'hochwohlgebohrner': 'hochwohlgeborner',
            'wolgebohrener': 'wohlgeborner',
            'hochwolgebohrener': 'hochwohlgeborner',
            'wohlgebohrener': 'wohlgeborner',
            'hochwohlgebohrener': 'hochwohlgeborner',
            'hochedelgebohrner': 'hochedelgeborner',
            'hochgelahrter': 'hochgelehrter',
            'hochgelährter': 'hochgelehrter',
            'hochgelahrtester': 'hochgelehrtester',
            'hochgelährtester': 'hochgelehrtester',
            'hochgelarter': 'hochgelehrter',
            'hochgelärter': 'hochgelehrter',
            'hochgelartester': 'hochgelehrtester',
            'hochgelärtester': 'hochgelehrtester',
            'hochgelerter': 'hochgelehrter',
            'hochgelertester': 'hochgelehrtester',
            'hochgeschätzer': 'hochgeschätzter',
            'hochgeschätzester': 'hochgeschätztester',
            'vatter': 'vater',
            'insonders': 'insonderst',
            'herr professor': 'professor',
            'herr cammerherr': 'cammerherr',
            'herr hofrath': 'hofrath',
            'herr bibliothecarius': 'bibliothecarius',
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
            root = None
        return root

    def get_type(self, root):
        if root in self.root_to_type:
            type = self.root_to_type[root]
        else:
            type = None
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

    def get_norma(self, word):
        norma = word
        if word in self.analogs:
            norma = self.analogs[word]
        return norma
