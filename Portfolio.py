import ffn

class Portfolio:

    def __init__(self, list):
        # initialize portfolio to list
        self.Portfolio = list

    def get_all(self):
        # returns all stocks in portfolio
        return Portfolio.list()

    def get_risk(self):
        # returns stocks with least risk
        return Allocator.least_risk()

    def get_growth(self):
        # returns stocks with highest growth potential
        return Allocator.growth()

    def get_value(self):
        # returns stocks with greatest value
        return Allocator.value()

    def get_best(self):
        # returns stocks that have low risk, high growth potential, and great value if any. Else, returns message...
        # ...stating that none were found
        risk_set = set(Allocator.least_risk())
        growth_set = set(Allocator.growth())
        value_set = set(Allocator.value())

        elements1 = risk_set.intersection(growth_set)

        if elements1 > null:
            elements2 = elements1.intersection(value_set)
            if elements2 > null:
                return elements1
            else:
                return "No best stocks found. Choose stocks individually from the list of least risk, growth, or value"
