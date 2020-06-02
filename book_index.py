
class Index:
	def __init__(self, pages):
		self.pages = pages

	def create_index(self):
		d = {}
		for i, page in enumerate(self.pages, 1):
			for s in page.split():
				if s not in d:
					d[s] = [i]
				else:
					d[s].append(i)
		return d



pages = ["Text of page one", "Text on page two", "This is on page three"]
ind = Index(pages)
print(ind.create_index())






