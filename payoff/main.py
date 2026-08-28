from initiator import Underlying, Option, Strategy

u = Underlying()
put = Option('put', 2.5, 100, 'long', 'Mar 26', 1, u, quantity=1)
s = Strategy([put], [u])

s.calculate_profit()
