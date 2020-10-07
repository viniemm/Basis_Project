import csv

from databases.QSet import QSet
from databases.Range import Range
import pandas as pd
import json


class QLibrary:
    def __init__(self):
        json.load("questions.json")






class QLibrary2:
    # this script will do the following.
    questions = dict()

    def addQLibrary(self, questionset, question, r):
        # adds a question to the QLibrary with the given range.
        self.questions.append(question, r)
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
            return self.questionSet(i)
        pass


class QLibrary:
    def __init__(self):
        df = pd.read_csv("questions.csv")
    def addSet(self, tag, qDict):
        class Question:


class Question:
    def __init__(self,question, qRange):
        self.question: str = question
        self.qRange: Ranges = qRange

class Ranges:
    @
    def __init__(self, listRange):

        self.listRange = listRange
        pass

    def toString(self):
        st = ""
        for options in self.listRange:
            st += options + ", "
        return st
    pass
