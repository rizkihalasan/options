from initiator import Underlying, Option, Strategy

u = Underlying(current_price=100, predicted_price=100, position='long')


options1 = Option('put', 'long', 95, 2.35, 'Mar 26', 1, u, quantity=1)
options2 = Option('call', 'long', 100, 2.7, 'Mar 26', 1, u, quantity=2)
options3 = Option('put', 'short', 95, 1.55, 'Mar 26', 1, u, quantity=4)
options4 = Option('put', 'long', 100, 3.7, 'Mar 26', 1, u, quantity=2)


options = [options1]
s = Strategy(options, u)

s.calculate_profit()
