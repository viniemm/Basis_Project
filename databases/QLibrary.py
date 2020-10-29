import pandas as pd


class QLibrary:
    def __init__(self):
        self.questions = pd.read_pickle("questions.pkl")
        self.col = self.questions.columns
        self.index = 0

    def add(self, rank: int, question: str, options: str):
        options = options.strip().split()
        row = [rank, question, options]
        df = dict(zip(self.col, row))
        self.questions = self.questions.append(df, ignore_index=True)

    def remove_single(self, question: str):
        self.questions.drop(self.questions[self.col[1]] == question)

    def remove(self, question_list: list):
        for x in question_list:
            self.remove(x)

    def find(self, question: str) -> list:
        return self.questions[self.col[1]] == question

    def replace(self, old_questions: list, rank: int, new_question: str, options: str):
        self.remove(old_questions)
        self.add(rank, new_question, options)

    def display(self):
        return self.questions.to_dict()

    def done(self):
        df = self.questions.drop_duplicates(subset=self.col[1])
        df.to_pickle("questions.pkl")