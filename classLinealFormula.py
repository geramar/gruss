from classFormula import Formula
import copy


class LinealFormula(Formula):
    def get_schema(self):
        schema = copy.deepcopy(self.types)
        for element in schema:
            if element == 'R':
                i = schema.index(element)
                schema[i] = str(schema[i]) + str(self.words[i].get_root())[0].upper()
        return '-'.join(map(str, schema))

    def __repr__(self):
        return str(self.words)
