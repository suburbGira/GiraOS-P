copyright="GIRAsoft 2017-2020." # copy protection
prodnum="GPN-PY-BE-GOSP09build1" # internal number for software cataloguing
bd="30 May 2020 @ 00:28 BST" # build date for reference
buildno="0.9 Beta, build 1.01 (9101)" # build information
ver_="Beta 0.9 (9101)" # version printed by ver
calculate = "calculate"   # -
test = "test"             #  |
verbose = "verbose"       #  |
changelog = "changelog"   #  |
ver = "ver"               #  |---- GIRAsoft Quoteless techology
sudo = "sudo"             #  |
buildtime = "buildtime"   #  |
buildcheck = "buildcheck" #  |
exit ="exit"              # _|
sudostatus=0 # if not declared here, causes a crash after input of developer id
#GGGGGGGGGGG IIIIIIIII RRRRRRRR AA                                       22222   00000   11   77777        22222   00000   22222   00000 
#G               I     R      R A A        sssss   ooooo   ffff    t    2     2 0    00 1 1       7       2     2 0    00 2     2 0    00
#G               I     R      R A  A      s     s o     o f    f ttttt       2  0   0 0   1      7             2  0   0 0      2  0   0 0
#G               I     RRRRRRRR A   A     s       o     o f        t        2   0  0  0   1     7             2   0  0  0     2   0  0  0
#G   GGGGGGG     I     R   R    AA   A     sssss  o     o ffff     t       2    0  0  0   1    7    -----    2    0  0  0    2    0  0  0
#G         G     I     R    R   A AA  A         s o     o f        t      2     0 0   0   1   7             2     0 0   0   2     0 0   0
#G         G     I     R     R  A   AA A  s     s o     o f        t     2      00    0   1   7            2      00    0  2      00    0
#GGGGGGGGGGG IIIIIIIII R      R A     AAA  sssss   ooooo  f        t    2222222  00000  11111 7           2222222  00000  2222222  00000  DO NOT SELL THIS SOFTWARE
import sys # enable exiting from within
print("GiraOS/P ver 0.8 build 1 -- copyright", copyright," You should have recieved a copy of the GNU GPL with this software. If not, you can find it on the Internet, or in most Linux software.") # print the copyright and gpl notice
print("DO NOT ATTEMPT TO SELL THIS SOFTWARE. IF YOU HAVE PAID FOR THIS SOFTWARE, PLEASE CONTACT greatgiratheepic@gmail.com!") # this was written in linux by one person - it should be free
while True:
	if copyright != "GIRAsoft 2017-2020.": # make sure we're good
		print("Error 03: Invalid Copyright message")
		sys.exit("exit::invalid copyright")
	if sudostatus != 1:
		command = input("Applications: ver, calc, sudo, stonks, exit >") # hooray for commands
	else:
		command = input("Applications: ver, calc, sudo, buildtime, buildcheck, stonks, exit >")

	if command == "ver": # app name: ver
		print ("GiraOS/P Version",ver_,"Copyright",copyright) # print the version - like winver
	elif command == "sudo":
		if sudostatus == 1:
			print("Already superuser; nothing to do")
		else:
			print("You are now a SUPERUSER. You now have priviledges to run superuser apps. Be careful...")
				sudostatus=1
	elif command == "exit":
		sys.exit("exit::user requested exit")
	elif command == "buildtime":
		if sudostatus != 1:
			print("Error 06: not a superuser")
		else:
			print ("Built", bd) # app name: buildtime
	elif command == "buildcheck":
		if sudostatus != 1:
			print("Error 06: not a superuser")
		else:
			print ("GiraOS/P version",buildno) # app name: buildcheck

	elif command=="stonks":
		# stonks - Tool to calculate if stonks have happened.
		# Copyright GIRAsoft, Inc. 2020.
		# Developed for GiraOS-P.
		instonks=y
		while instonks=y:
			stonks1=input("Input first number: ")
			stonks2=input("Now input second number: ")
			if stonks1 > stonks2:
				print("Not Stonks")
			elif stonks2 > stonks1:
				print("Stonks")
			elif stonks1 == stonks2:
				print("Neither Stonks or Not Stonks")
			instonks=input("Another? (y/n): ")
			if instonks != y:
				if instonks != n:
					print("Invalid answer, assuming no.")
					instonks = n
		
	elif command=="calc":
		# GIRAsoft Calculator copyight GIRAsoft, Inc. 2018.
		# Developed for use in GiraOS-P.
		y="y"
		n="n"
		add="add"
		sub="sub"
		mul="mul"
		div="div"
		calculate = y
		while calculate==y:
			num1=input("Enter first number. >")
			operand=input("Enter operand (add for add, sub for subtract, mul for multiply or div for divide) >")
			num2=input("Enter second number. >")
			if operand == "add":
				out=(num1+num2)
			elif operand == "sub":
				out=(num1-num2)
			elif operand == "div":
				out=(num1/num2)
			elif operand == "mul":
				out=(num1*num2)
			else:
				print("Error 07: Invalid operand")
			print("Your answer is:", out)
			calculate=input("Perform another calculation? (y/n) >")
			if calculate != "y" and calculate != "n":
				print("Error 08: Invalid answer.")
	else:
		print("Error 05: Invalid command") # only applies for numbers (and ver for some reason); text causes a crash
