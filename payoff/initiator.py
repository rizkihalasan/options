import matplotlib.pyplot as plt
import numpy as np

LONG = 'long'
SHORT = 'short'
CALL = 'call'
PUT = 'put'

class Underlying:
    def __init__(self, price=100, position=LONG, quantity=1):
        self.price = price
        self.position = position
        self.quantity = quantity

class Option:
    def __init__(self, call_or_put, premium, strike_price, position, expiry, volatility, underlying, quantity=1):
        self.call_or_put = call_or_put
        self.premium = premium
        self.strike_price = strike_price
        self.position = position
        self.expiry = expiry
        self.volatility = volatility
        self.underlying = underlying
        self.quantity = quantity

class Strategy:
    def __init__(self, options=None, underlyings=None):
        self.options = options
        self.underlyings = underlyings
    
    def calculate_profit(self):
        spot_prices = np.linspace(80, 120, 100)
        for option in self.options:
            if option.call_or_put == CALL:
                profit = np.maximum(-option.premium, spot_prices - option.strike_price)
            else:
                profit = np.maximum(-option.premium, option.strike_price - spot_prices)

        plt.figure(figsize=(10,6))

        plt.plot(spot_prices, profit, color="green", lw=2.5)

        
        plt.show()




    


