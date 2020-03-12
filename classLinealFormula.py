from classFormula import Formula


class LinealFormula(Formula):
    def get_schema(self):
        for element in self.schema:
            if element == 'R':
                i = self.schema.index(element)
                self.schema[i] = str(self.schema[i]) + str(self.words[i].get_root())[0].upper()
        return '-'.join(map(str, self.schema))

    def __repr__(self):
        return str(self.words)
