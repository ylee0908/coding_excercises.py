class StockTrade:
	def __init__(self):
		self.stack = []
		self.max = []

	def add_trade(self, ticker, n):
		self.stack.append((ticker, n))

		cur_max = self.get_max()
		if cur_max is None or n > cur_max:
			self.max.append((ticker, n))

	def print_trade(self):
		print (self.stack)

	def execute_trade(self):
		if self.stack[-1] == self.max[-1]:
			_max, _trade = self.max.pop(), self.stack.pop()
			print(_trade)
			return _max, _trade

		else:
			to_print = self.stack.pop()
			print(to_print)
			return to_print

	def get_max(self):
		if len(self.max) == 0:
			return None
		else:
			return self.max[-1][1]





stock = StockTrade()
stock.add_trade("IBM", 1)
stock.add_trade("GOOG", 2)
stock.add_trade("TSLA", 2)
stock.add_trade("BIM", 3)
print(stock.get_max()) # should be 3
stock.execute_trade()
print(stock.get_max()) # should be 2
stock.execute_trade()
print(stock.get_max()) # should be 2


