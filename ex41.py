# __coding: utf-8__

'''
来自25号行星的哥顿人

函数作为对象，可以如同变量一般传递。
这一节是函数作为对象的练习。

同时
函数可以放在数组中。

这是一种实现“有限状态机”的方式
'''

from sys import exit
from random import randint

def death():
	quips = ["You died. You kinda suck at this.",
		"Nice job, you died ...jackass.",
		"Such a luser.",
		"I have a small puppy that's better at this."]

	print quips[randint(0, len(quips)-1)]
	exit(1)

def central_corridor():
	print "The Gothons of Planet Percal #25 have invaded your ship and destoryed."
	print "your entire crew. You are the last surviving member and your last"
	print "mission is to get the neutron destruct bomb from the Weapon Armory,"
	print "put it in the breidge, and blow the ship up after getting into an "
	print "escape pod."
	print "\n"
	print "You're running down the central corridor to the Weapons Armory when"
	print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
	print "flowing around his hate filled body. He's blocking the door to the"
	print "Armory and about to pull a weapon to blast you."

	action = raw_input("> ")

	if action == "shoot!":
		print "Quick on the draw you yank out your blaster and fire it at Gothon."
		print "His clown costume is flowing and moving around his body, which throws"
		print "off your aim. Your laser hits his mother bought him, which"
		print "makes him fly into an insane rage and blast you repeatedly in the face until"
		print "you are dead. Then he eats you."
		return 'death'

	elif action == "dodge!":
		print "Like a world class boxer you dodge, weave, slip and slide right"
		print "as the Gothon's blaster cranks a laser past you head."
		print "In the middle of your artful dodge your foot slips and you"
		print "bang your head on the metal wall and pass out."
		print "You wake up shortly after only to die as the Gothon stomps on"
		print "your head and eats you."
		return 'death'

	elif action == "tell a joke":
		print "Lucky for you they made you learn Gothon insults in the academy."
		print "You tell the one Gothon joke you know:"
		print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gut ubhfr."
		print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
		print "While he's laughing you run up and shoot him square in the head"
		print "putting him down, then jump through the Weapon Armory door."
		return 'laser_weapon_armory'

	else:
		print "DOES NOT COMPUTE!"
		return 'central_corridor'

def laser_weapon_armory():
	print "laser_weapon_armory"
	code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
	guess = raw_input("[keypad]> ")
	guesses = 0

	while guess != code and guesses < 10:
		print "BZZZZEDDD!"
		guesses += 1
		guess = raw_input("[keypad]> ")

	if guess == code:
		print 'now to the_bridge'
		return 'the_bridge'
	else:
		print "You died."
		return 'death'

def the_bridge():
	print "This is the_bridge."
	print "Please input what you want to do."
	action = raw_input("> ")

	if action == "throw the bomb":
		print "The bomb was blow_up."
		print "It goes off."
		return 'death'

	elif action == "slowly place the bomb":
		print "You point your blaster at the bomb under your arm"
		print "You escape_pod"
		return "escape_pod"

	else:
		print "DOES NOT COMPUTE!"
		return "the_bridge"


def escape_pod():
	print "This is escape_pod."
	good_pod  = randint(1, 5)
	guess = raw_input("[pd #]> ")

	if int(guess) != good_pod:
		print "you dead."
		return 'death'
	else:
		print "time. You won!"
		exit(0)

ROOMS = {
	'death': death,
	'central_corridor': central_corridor,
	'laser_weapon_armory': laser_weapon_armory,
	'the_bridge': the_bridge,
	'escape_pod': escape_pod
}

def runner(map, start):
	next = start

	while True:
		room = map[next]
		print "\n----------"
		next = room()

START_ROOM = 'central_corridor'
runner(ROOMS, START_ROOM)