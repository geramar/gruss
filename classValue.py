class Value:
    def __init__(self, value, beginning, ending):
        self.value = value
        self.beginning = beginning
        self.ending = ending
    def __repr__(self):
        if self.value == 1:
            return 'Totally correct'
        elif self.value == (1, 0):
            return 'Correct until ' + str(self.ending + 1) + 'th word'
        elif self.value == (0, 1):
            return 'Correct starting from ' + str(self.beginning + 1)
        elif self.value == (0, 0):
            return 'Correct starting from ' + str(self.beginning + 1) + 'th word ' + 'ending at ' + str(
            self.ending + 1) + 'th word'
        elif self.value == -1:
            return 'illineal'
        else:
            return 'not correct'