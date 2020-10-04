class Range:
    def __init__(self, listRange):

        self.listRange = listRange
        pass

    def toString(self):
        st = ""
        for options in self.listRange:
            st += options + ", "
        return st
    pass
