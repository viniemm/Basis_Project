import csv
import pandas as pd
import json
from multipledispatch import dispatch


class QRange:
    @dispatch(list)
    def __init__(self, buttons):
        self.type_range = "buttons"
        self.buttons = buttons

    @dispatch(int, int)
    def __init__(self, i, j):
        self.type_range = "slider"
        self.i = i
        self.j = j

    @dispatch()
    def __init__(self):
        self.type_range = "user_value"


class Question:
    def __init__(self, question: str, ran: QRange):
        self.question: str = question
        self.ran: QRange = ran


class QSet:
    @dispatch(str, int, list)
    def __init__(self, name, priority, ques):
        self.ques: list = ques
        self.name: str = name
        self.priority: int = priority

    @dispatch(str, int)
    def __init__(self, name, priority):
        self.name: str = name
        self.priority: int = priority


class QLibrary:
    def __init__(self):
        df = pd.read_csv("questions.csv")

    def add(self, qset):
        pass

    def replace(self, qset_name, old_question, new_question, new_range):
        pass

    def find(self, question):
        pass

    def display(self):
        pass

    @dispatch(str)
    def remove(self, question):
        pass

    @dispatch(QSet)
    def remove(self, question):
        pass

    def exists(self):
        pass

    def clear(self, passkey):
        pass

    def modify(self, question, new_options):
        pass
