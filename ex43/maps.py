# __coding: utf-8__
# /usr/local/Cellar python
''' this is test module '''

import sys

''' 全局变量 '''

class maps(object):
	''' The games maps '''
	def __init__(self):
		pass

	def GoldRoom(self):
		print 'Its GoldRoom.'
		pass

	def KoiPondRoom(self):
		print 'Its KoiPondRoom.'
		pass

def test():
	print "maps module test."

if __name__ == '__main__':
	test()
