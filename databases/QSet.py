from databases.Range import Range


class QSet:
    def __init__(self, question, r: Range):
        self.question = question
        self.r = r
        pass

    #@property
    def toString(self):
        return self.question + "Options are: " + self.r.toString()
