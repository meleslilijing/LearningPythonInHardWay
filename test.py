class testClass(object):
	def __init__(self):
		self.a = "as"

	def play(self):
		# self.b = getattr(self, a)
		print self.a

obj = testClass()
obj.play()