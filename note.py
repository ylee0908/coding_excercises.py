class Note:
	def __init__(self, title, body, nickname):
		self.title = title
		self.body = body
		self.nickname = nickname

class NoteApp:
	d = dict()

	def _add(self, title, body, nickname):
		new_note = Note(title, body, nickname)
		self.d[nickname] = new_note.title, new_note.body

	def get(self, nickname):
		if nickname in self.d:
			print(self.d[nickname])
			return

	def print_list(self):
		print (list(self.d.keys()))

note = NoteApp()
note._add('one', 'body1', "first day")
note.get('first day')
note._add('two', 'body2', 'Second day')
note.print_list()
