import ffn
import matplotlib.pyplot as plt
from empyrical import alpha_beta
import numpy as np

class Allocator:

    def __init__(self):
        self.Allocator = 0

    def get_price(self, set_of_tickers, start_date):
        # returns the price of stocks with given tickers from given start date
        if start_date == 0:
            price = ffn.get(set_of_tickers)
        else:
            price = ffn.get(set_of_tickers, start=start_date)
        return price

    def get_average_return(self, tickers, start_date):
        # returns the average return of stocks with given tickers from the given start date
        price = get_price(tickers, start_date)
        average_return = price.pct_change().mean()
        return average_return

    def get_covariance(self, tickers):
        # returns the covariance of the stocks with given tickers from the given start date
        price = get_price(tickers, 0)
        covariance = price.pct_change().cov()
        return covariance

    def set_portfolio_weights(self, weights):
        #returns the portfolio weights as an array
        return np.asarray(weights)


    def get_alpha(self, ticker, start_date):
        # returns alpha which is defined as the excess return of an investment relative to the S&P500 (ticker: 'spy')
        # an alpha of 0.5 means that the stock has outperformed the S&P500 by 0.5%
        spy = get_price({'spy'}, start=start_date)
        ticker_price = get_price(ticker, start=start_date)
        alpha, beta = alpha_beta(ticker_price, spy)
        return alpha

    def get_beta(self, ticker, start_date):
        # returns beta which is a measure of the stock's volatility relative to the S&P500 (ticker: 'spy)
        # beta > 1 means stock is more volatile than spy, beta < 1 means stock is less volatile than spy
        spy = get_price({'spy'}, start=start_date)
        ticker_price = get_price(ticker, start=start_date)
        alpha, beta = alpha_beta(ticker_price, spy)
        return beta

    def portfolio_return(self, tickers, weights):
        # returns the return of the portfolio taking into account the portfolio weights
        # 252.25 is the average number of days that the market is open in a given year (253 in leap years & 252...
        # ...otherwise)
        return np.sum(get_average_return(tickers) * set_portfolio_weights(weights)) * 252.25

    # def volatility(self): --YET TO BE COMPLETED
    # Note to self: to complete the above, need to calculate standard deviation

    def mean_variance(self, tickers, start_date):
        # returns the mean variance of the tickers given
        returns = get_price(tickers, start_date).to_returns.dropna()
        mean_var = returns.calc_mean_var_weights().as_format('.2%')
        return mean_var

    def relative_performance_graph(self, tickers, start_date):
        # plots a rebase graph among stocks with tickers given
        rel = get_price(tickers, start_date).rebase().plot(figsize=(10, 5))
        rel.show()

    def histogram_of_returns(self, tickers, start_date):
        # plots a histogram of the given stocks
        histogram = get_price(tickers, start_date).hist()
        return histogram

    def statistics(self, tickers, start_date):
        # computes and displays common statistics of stocks with tickers given
        stats = get_price(tickers, start_date).calc_stats()
        stats.display()

    def correlations(self, tickers, start_date):
        # returns the correlations among stocks with tickers given
        # if cor = +1, then stocks are perfectly positively correlated
        # if cor = -1, then stocks are perfectly negatively correlated
        # if cor = 0, then stocks are not correlated at all
        cor = get_price(tickers, start_date).corr.asformat('.2f')
        print(cor)

    def heat_map_visualization(self, tickers, start_date):
        # plots a heat map of correlations among the stocks with tickers given
        hm = get_price(tickers, start_date).plot_corr_heatmap()
        hm.show()

    def least_risk(self, list):
        # returns the list of least risky stocks among those in the list given
        length = list.length()
        less_risk = []
        for i in range(0, length):
            if get_beta(list[i], 0) < 1:
                less_risk.append(list[i])
            i += 1
        return less_risk

    def growth(self, list):
        # returns the list of growth stocks among those in the list given
        length = list.length()
        growth_stocks = []
        for i in range(0, length):
            if get_alpha(list[i], 0) < 1:
                growth_stocks.append(list[i])
            i += 1
        return growth_stocks

    # def value(self, list): --YET TO BE COMPLETED
    # Note to self: use P/E, EPS, Revenue over Earnings

    # Advanced things to complete if possible:
    # 1) For an inputted avg. return, recommend stocks that will give that expected return
    # 2) Use correlation function to construct portfolio in which individual stocks are less correlated to each other...
    #    ...in order to decrease portfolio risk. Note: can also use beta function for this
