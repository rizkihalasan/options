from initiator import Underlying, Option, Strategy

u = Underlying(current_price=100, predicted_price=100, position='long')


options1 = Option('put', 'long', 100, 2.35, 'Mar 26', 1, u, quantity=1)
options2 = Option('call', 'short', 100, 2.7, 'Mar 26', 1, u, quantity=1)


options = [options1, options2]
s = Strategy(options, u)

s.calculate_profit()
