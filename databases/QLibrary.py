import csv

from databases.QSet import QSet
from databases.Range import Range


class QLibrary:
    # this script will do the following.
    questions = list()

    def addQLibrary(self, question, r):
        # adds a question to the QLibrary with the given range.
        list.append(question, r)
        pass

    def removeQLibrary(self, question):
        # removes a question completely from the QLibrary
        pass

    def modifyQLibrary(self, question, newRange):
        # modifies a question in the QLibrary by replacing the old range with the new one.
        pass

    def questionSet(self, i):
        return QSet(i)
        pass

    range0 = Range(["Novice", "Experienced"])
    set0 = QSet("Are you a Novice or Experienced investor?", range0)

    def set(self, i):
        if i == "exit":
            return None
        elif i == 0:
            return self.set0
        else:
            return self.questionSet(self, self.i)
        pass
