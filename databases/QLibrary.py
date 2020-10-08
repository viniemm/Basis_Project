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
    def __init__(self):
        pass


class QLibrary:
    def __init__(self):
        df = pd.read_csv("questions.csv")

    def add(self, question, options):
        pass

    def replace(self, old_question, new_question, new_options):
        pass

    def find(self, question):
        pass

    def display(self):
        pass

    def get(self):
        pass

    def remove(self):
        pass

    def exists(self):
        pass

    def clear(self, passkey):
        pass

    def modify(self, question, new_options):
        pass
