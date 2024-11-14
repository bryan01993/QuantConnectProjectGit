import scipy.stats as sp
import numpy as np

class BsmModel:
    def __init__(self, option_type, price, strike, interest_rate, expiry, volatility, dividend_yield=0):
        self.s = price  # Underlying asset price
        self.k = strike  # Option strike K
        self.r = interest_rate  # Continuous risk fee rate
        self.q = dividend_yield  # Dividend continuous rate
        self.T = expiry / 365  # time to expiry (year)
        self.sigma = volatility  # Underlying volatility
        self.type = option_type  # option type "p" put option "c" call option
        # TODO Add object OptionRight into type

    def n(self, d):
        # cumulative probability distribution function of standard normal distribution
        return sp.norm.cdf(d)

    def dn(self, d):
        # the first order derivative of n(d)
        return sp.norm.pdf(d)

    def d1(self):
        return (np.log(self.s / self.k) + (self.r - self.q + self.sigma ** 2 * 0.5) * self.T) / (
                    self.sigma * np.sqrt(self.T))

    def d2(self):
        return (np.log(self.s / self.k) + (self.r - self.q - self.sigma ** 2 * 0.5) * self.T) / (
                    self.sigma * np.sqrt(self.T))

    def bsm_price(self):
        d1 = self.d1()
        d2 = d1 - self.sigma * np.sqrt(self.T)
        if self.type == 'c':
            call_price = round(np.exp(-self.r * self.T) * (
                        self.s * np.exp((self.r - self.q) * self.T) * self.n(d1) - self.k * self.n(d2)), 2)
            print(f"call_price = {round(call_price, 2)}")
            return call_price
        if self.type == 'p':
            put_price = round(np.exp(-self.r * self.T) * (
                    self.k * self.n(-d2) - (self.s * np.exp((self.r - self.q) * self.T) * self.n(-d1))), 2)
            print(f"put_price = {round(put_price, 2)}")
            return put_price
        print("option type can only be c or p")

# For Local Testing
a = BsmModel('c', 42, 35, 0.1, 90.0, 0.2)
a.bsm_price()
