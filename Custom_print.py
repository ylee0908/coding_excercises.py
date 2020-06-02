class CustomPrint:
	def __init__(self, wrapping, uppercase, replacement):
		self.wrapping = wrapping
		self.uppercase = uppercase
		self.replacement = replacement


	def string_process(self, s):
		if self.wrapping is True:
			n = len(s)//13
			res = ""
			for i in range(n+1):
				res += s[13*i : 13*(i+1)] + '\n'
			s = res
		if self.uppercase is True:
			s = s.upper()
		if self.replacement != None:
			if self.uppercase is True:
				s = s.replace(self.replacement[0].upper(), self.replacement[1].upper())
			else:
				s = s.replace(self.replacement[0].lower(), self.replacement[1].lower())
		return s


line = CustomPrint(True, True, ('abc', 'back'))
print(line.string_process("Children are abc to school but they are incapable to keep social distance."))
