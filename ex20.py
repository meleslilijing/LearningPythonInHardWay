# __coding:utf-8__
'''
函数和文件:

需要注意
file.seek()
file.tell()
这两个函数。

file.seek(p, n): 设置文件读取指针到p位置，并往后相对移动n个位置。
file.tell(): 返回文件读取指针的当前位置。

'''

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)
print current_file.tell()

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)