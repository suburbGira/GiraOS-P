import sys # enable exiting from within
print "Gira OS/P ver 0.1, copyright GIRAsoft 2017-2020"
print "NOTE: Due to Python being weird, please use ONLY numbers as input."
while True:
	command = input("Press 1 for test or 2 to exit: ")
	if command == 1:
		print("Testing")
		print("esting")
		print("sting")
		print("ting")
		print("ing")
		print("ng")
		print("g")
		print("done executing")
	elif command == 2:
		sys.exit("exit::user requested exit")
	else:
		print("Invalid command.") # only applies for numbers; text causes a crash
