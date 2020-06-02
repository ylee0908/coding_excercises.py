class PhoneBook:
	def __init__(self):
		self.d = dict()
		self.last_id = 0


	def add_contact(self, name, phone, email):
		new_id = self.last_id + 1
		self.last_id = new_id
		self.d[new_id] = (name, phone, email)

	def modify_contact(self, id, name, phone, email):
		search_result = self.search_contact(id)
		if search_result:
			self.d[id] = (name, phone, email)
			print(f"ID No {id} updated")
			return self.print_all_contact_details()
		else:
			self.add_contact(name, phone, email)
			print(f"ID No {id} available. New contact list updated")
			return self.print_all_contact_details()

	def print_ids(self):
		print(list(self.d))
		return

	def print_all_contact_details(self):
		print(self.d)

	def search_contact(self, id):
		if id in self.d:
			print(f"ID existed for {self.d[id][0]}")
			return True
		else:
			return False


phonebook = PhoneBook()
phonebook.add_contact("Yuna", 333, 'y@gmail.com')
phonebook.add_contact("Aaron", 555, 'a@gmail.com')
phonebook.add_contact("Dave", 777, 'd@gmail.com')

phonebook.print_ids()
phonebook.print_all_contact_details()
phonebook.modify_contact(1, 'Alice', 999, 'a@gmail.com')
phonebook.modify_contact(10, 'James', 1000, 'j@gmail.com')

