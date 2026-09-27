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


# Case-insensitive alias for Linux/QuantConnect Cloud compatibility
BSMModel = BsmModel


import math
from typing import Optional, Union

def fast_norm_cdf(x: float) -> float:
    """Standard normal cumulative distribution function using math.erf (100x faster than scipy)."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def fast_norm_pdf(x: float) -> float:
    """Standard normal probability density function."""
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)

def fast_bs_price(right: Union[int, str], S: float, K: float, T: float, r: float, sigma: float) -> float:
    """Fast Black-Scholes formula price for Call and Put options."""
    if T <= 0.0 or sigma <= 0.0 or S <= 0.0 or K <= 0.0:
        return 0.0
    d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    is_call = (right == 0 or str(right).lower() in ("c", "call", "optionright.call"))
    if is_call:
        return S * fast_norm_cdf(d1) - K * math.exp(-r * T) * fast_norm_cdf(d2)
    else:
        return K * math.exp(-r * T) * fast_norm_cdf(-d2) - S * fast_norm_cdf(-d1)

def fast_vega(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """Calculates Option Vega."""
    if T <= 0.0 or sigma <= 0.0 or S <= 0.0 or K <= 0.0:
        return 0.0
    d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
    return S * fast_norm_pdf(d1) * math.sqrt(T)

def fast_implied_volatility_newton(right: Union[int, str], S: float, K: float, T: float, r: float, market_price: float) -> Optional[float]:
    """Fast Newton-Raphson solver for Black-Scholes implied volatility."""
    if market_price <= 0.0 or S <= 0.0 or K <= 0.0 or T <= 0.0:
        return None
    sigma = 0.30
    for _ in range(15):
        price = fast_bs_price(right, S, K, T, r, sigma)
        diff = price - market_price
        if abs(diff) < 1e-4:
            return sigma
        v = fast_vega(S, K, T, r, sigma)
        if v < 1e-6:
            break
        sigma = sigma - diff / v
        if sigma <= 0.01:
            sigma = 0.01
        elif sigma > 5.0:
            sigma = 5.0
    return sigma if abs(fast_bs_price(right, S, K, T, r, sigma) - market_price) < 0.05 else None


if __name__ == "__main__":
    a = BsmModel('c', 42, 35, 0.1, 90.0, 0.2)
    a.bsm_price()
