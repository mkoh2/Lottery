from random import randint

def play():
	play_a = int(raw_input("How many times do you want to play? : "))
	total = 0
	
	while total < play_a:
		draw = int(total) + 1
		print "Draw number: %d" % draw
		print "> %d, %d, %d, %d, %d | %d" % (randint(0,99), randint(0,99), 
		randint(0,99), randint(0,99), randint(0,99), randint(0,99))
		total += 1
	else:
		exit(0)
	
def start():
	print
	print "Welcome to the Random Lottery Generator!"
	print "Let's get started.\n"
	print "-" * 10
	print
	play()

start()