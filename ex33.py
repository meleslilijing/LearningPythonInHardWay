#__coding:utf-8__
''' while-loop '''

def doWhile(n):
	i = 0
	while i < n:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i +1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

numbers = []

doWhile(3)

print "The numbers: "

for num in numbers:
	print num

