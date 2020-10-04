from databases.QLibrary import QLibrary


class Test:
    def __init__(self):
        self.lib: QLibrary = QLibrary()
        self.i = 0
        self.solutionSet = list()
        print("Answer the following questions and type exit whenever you want to stop\n")
        while self.i != "exit":
            self.qset = self.lib.set(self.i)
            self.i = input(self.qset.toString()).lower()
            self.solutionSet.append(self.i)
            pass
        print(*self.solutionSet, sep=", ")
        pass

    pass


Test()

pass
