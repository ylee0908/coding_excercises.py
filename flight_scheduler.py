class Flights:
	flights = {}

	def add_flight(self, beginning, end):
		if beginning not in self.flights:
			self.flights[beginning] = [end]
		else:
			self.flights[beginning].append(end)

	def print_all(self):
		print(self.flights)

	def find_route(self, beginning, end):
		visited = {}
		if self.find_route_recursive(beginning, end, visited):
			return True
		else:
			return False

	def find_route_recursive(self, beginning, end, visited):
		print([beginning, end])
		visited[beginning] = 0
		for destination in self.flights[beginning]:
			if end == destination:
				return True
			elif destination not in visited and destination in self.flights:
				if self.find_route_recursive(destination, end, visited):
					return True
		del visited[beginning]


flights = Flights()
flights.add_flight("Paris", "London")
flights.add_flight("Paris", "Shanghai")
flights.add_flight("Shanghai", "Paris")
flights.add_flight("Seattle", "San Francisco")
flights.add_flight("Seattle", "New York")
flights.add_flight("New York", "Seattle")
flights.add_flight("Shanghi", "Paris")
flights.add_flight("New York", "Seoul")
flights.add_flight("London", "Seoul")
flights.print_all()
print(flights.find_route("Paris", "Tokyo")) # should return false
print(flights.find_route("Seattle", "Seoul")) # should return true
