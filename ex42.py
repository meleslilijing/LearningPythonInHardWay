from sys import exit
from random import randint

class Game(object):

	def __init__(self, start):
		self.quips = [
			"You died. You kinda suck at this.",
			"Your mom would be pround. If she were smarter.",
			"Such a luser.",
			"I have a small puppy that's better at this."
		]

		self.start = start
		
# class TheThing(object):

# 	def __init__(self):
# 		self.number = 0

# 	def some_function(self):
# 		print "I got called."

# 	def add_me_up(self, more):
# 		self.number += more
# 		return self.number

# # two different things
# a = TheThing()
# b = TheThing()

# a.some_function()
# b.some_function()

# print a.add_me_up(20)
# print a.add_me_up(20)
# print b.add_me_up(30)
# print b.add_me_up(30)

# print a.number
# print b.number

