class Browser:
	stack = []
	def visit(self, url):
		self.stack.append(url)

	def back(self):
		last_visit = self.stack.pop()
		print(f"last visit: {last_visit}")


browser = Browser()
browser.visit('www.google.com')
browser.visit("www.yahoo.com")
browser.visit('www.netflix.com')

browser.back()
browser.back()
browser.back()
