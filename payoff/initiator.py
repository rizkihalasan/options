import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import math
from matplotlib.widgets import Slider, Button

LONG = 'long'
SHORT = 'short'
CALL = 'call'
PUT = 'put'

class Underlying:
    def __init__(self, current_price=100, predicted_price=100, position=LONG, quantity=1):
        self.current_price = current_price
        self.predicted_price = predicted_price
        self.position = position
        self.quantity = quantity

class Option:
    def __init__(self, call_or_put, position, strike_price, premium, expiry, volatility, underlying, quantity=1):
        self.call_or_put = call_or_put
        self.position = position
        self.strike_price = strike_price
        self.premium = premium
        self.expiry = expiry
        self.volatility = volatility
        self.underlying = underlying
        self.quantity = quantity

class Strategy:
    def __init__(self, options=None, underlying=None):
        self.options = options
        self.underlying = underlying
    
    def calculate_profit(self, left_x = None, right_x = None):
        min_threshold = 0.80
        max_threshold = 1.20
        profit = 0
        if left_x and right_x:
            spot_prices = np.linspace(left_x, right_x, 100)
        elif not self.underlying:
            spot_prices = np.linspace(80, 120, 100)
            
        else:
            spot_prices = np.linspace(math.floor(self.underlying.current_price * min_threshold), math.ceil(self.underlying.current_price * max_threshold), round(self.underlying.current_price))
            if self.underlying.position == LONG:
                profit += spot_prices - self.underlying.current_price
            elif self.underlying.position == SHORT:
                profit += self.underlying.current_price - spot_prices

        for option in self.options:
            if option.position == LONG:
                if option.call_or_put == CALL:
                    profit += (np.maximum(-option.premium, spot_prices - option.strike_price - option.premium) *  option.quantity)
                elif option.call_or_put == PUT:
                    profit += (np.maximum(-option.premium, option.strike_price - spot_prices - option.premium) *  option.quantity)
            elif option.position == SHORT:
                if option.call_or_put == CALL:
                    profit += (-np.maximum(-option.premium, spot_prices - option.strike_price - option.premium) * option.quantity)
                elif option.call_or_put == PUT:
                    profit += (-np.maximum(-option.premium, option.strike_price - spot_prices - option.premium) * option.quantity)

        plt.figure(figsize=(10,6))

        plt.plot(spot_prices, profit, color="green", lw=2.5)
        plt.axhline(0, color="black", linestyle="--", alpha=0.5)

        ax = plt.gca()
        ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

        plt.xlabel("Stock Price")
        plt.ylabel("Profit")

        plt.show()
        plt.ion()




    


