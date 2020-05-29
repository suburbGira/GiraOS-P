copyright="GIRAsoft 2017/2018." # copy protection
prodnum="GPN-PY-BE-GOSP06build1" # internal number for software cataloguing
key="GIRA-SOFT" # product key - antipiracy
devidsub=1963 # developer id list here - makes sure only devs can access beta
deviddark=2729
devidshel=3207
devidscythe=4088
bd="1 Mar 2018 @ 17:47 GMT" # build date for reference
buildno="0.7 Beta, build 1.39 (7139)" # build information
ver="Beta 0.7 (7139)" # version printed by ver
# GIRASOFT = "GIRASOFT" # its free anyways, we dont need no product key... it was just so i could say 'hey look, my software can has product key!'
test = "test"             # _
verbose = "verbose"       #  |
changelog = "changelog"   #  |
ver = "ver"               #  |---- GIRAsoft Quoteless techology
sudo = "sudo"             #  |
buildtime = "buildtime"   #  |
buildcheck = "buildcheck" # _|
sudostatus=0 # if not declared here, causes a crash after input of developer id
#GGGGGGGGGGG IIIIIIIII RRRRRRRR AA                                       22222   00000   11   77777        22222   00000   11    88888
#G               I     R      R A A        sssss   ooooo   ffff    t    2     2 0    00 1 1       7       2     2 0    00 1 1   8     8
#G               I     R      R A  A      s     s o     o f    f ttttt       2  0   0 0   1      7             2  0   0 0   1   8     8
#G               I     RRRRRRRR A   A     s       o     o f        t        2   0  0  0   1     7             2   0  0  0   1   8     8
#G   GGGGGGG     I     R   R    AA   A     sssss  o     o ffff     t       2    0  0  0   1    7    -----    2    0  0  0   1    88888
#G         G     I     R    R   A AA  A         s o     o f        t      2     0 0   0   1   7             2     0 0   0   1   8     8
#G         G     I     R     R  A   AA A  s     s o     o f        t     2      00    0   1   7            2      00    0   1   8     8
#GGGGGGGGGGG IIIIIIIII R      R A     AAA  sssss   ooooo  f        t    2222222  00000  11111 7           2222222  00000  11111  88888   DO NOT SELL THIS SOFTWARE
import sys # enable exiting from within
print "GiraOS/P ver 0.7 build 1 -- copyright", copyright," You should have recieved a copy of the GNU GPL with this software. If not, you can find it on the Internet, or in most Linux software." # print the copyright and gpl notice
print("DO NOT ATTEMPT TO SELL THIS SOFTWARE. IF YOU HAVE PAID FOR THIS SOFTWARE, PLEASE CONTACT greatgiratheepic@gmail.com!") # this was written in linux by one person - it should be free
# print("NOTE: Please input all non-numeric commands inside double quotes (\").") # FINALLY fixed
# checkkey=input("Enter your product key >") # make sure this is legal
if 621743512==234234:
#	print("Error 01: Invalid key") # o noez, we're illegal
#	sys.exit("exit::invalid key")
	print("bjhgj")
else:
	checkid=input("Enter your developer ID. >") # devs only
	if checkid != devidsub:
		if checkid != deviddark:
			if checkid != devidshel:
				if checkid != devidscythe:
					print("Error 02: Invalid developer ID")
					sys.exit("exit::invalid developer ID")
while True:
	if copyright != "GIRAsoft 2017/2018.": # make sure we're good
		print("Error 03: Invalid Copyright message")
		sys.exit("exit::invalid copyright")
	if sudostatus != 1:
		command = input("Applications: test, verbose, changelog, ver, sudo, exit >") # hooray for commands
	else:
		command = input("Applications: test, verbose, changelog, ver, sudo, buildtime, buildcheck, exit >")
	if command == "test":
		print("Testing") # app name: test
		print("esting")
		print("sting")
		print("ting")
		print("ing")
		print("ng")
		print("g")
		print("done executing")
	elif command == "verbose":
		print("Expression of surprise or astonishment at the unintended performance of an undefined action!") # app name: verbose
		print("I regret that the system which processes input as a series of ones and zeroes known as binary belonging to the organism known as a human who has been given the designation of me has performed an action which was not intended to be performed by its manufacturers!")
		print("Additionally, the aforementioned problem has caused it to magnetise small spinning discs inside it in such a way that any data stored on them has been removed!")
		print("However, to combat this from happening, I possessed a computer program which is designed to prevent this type of error from happening by stopping malicious data from editing the performance of my device which processes input as a series of ones and zeros known as binary!")
		print("I regret to inform you that the aforementioned computer program possessed by you is currently insufficient to prevent the loss of data due to the unintended magnetisation and/or demagnetisation of small spinning discs inside the system which processes input as a series of ones and zeroes known as binary belonging to the organism known as a human who has been given the designation of you!")
		print("The organism known as a human who has been given the designation of you possess the requirement to purchase a computer program which has ben given the name of Protegent 360 Security by its creators, Unistal Global Inc. which is designed to prevent malicious computer programs from entering your system which processes input as a series of ones and zeroes known as binary!")
		print("The only computer software currently existing in the planet we are standing on which possesses the power to prevent the unintended magnetisation and/or demagnetisation of small spinning discs inside a system which processes input as a series of ones and zeroes known as binary in such a way that any data stored on them is lost!")
		print("Use the organ known as a brain to perform the action of thinking beyond computer programs which prevent malicious computer programs entering systems which process input as a series of ones and zeros known as binary!")
		print("Use the organ known as a brain to perform the action of thinking about a computer program which has ben given the name of Protegent 360 Security by its creators, Unistal Global Inc. which is designed to prevent malicious computer programs from entering your system which processes input as a series of ones and zeroes known as binary!")
	elif command == "changelog":
		print("     Ver 0.4      ") # app name: changelog
		print(" Added copyright  ")
		print("Added product num.")
		print("LOADS of bugfixes ")
		print("Removed changelog ")
		print("==================")
		ask=input("Show more? 1:Yes 2:No >")
		if ask==1:
			print("     Ver 0.3      ")
			print("Added logo in code")
			print("==================")
			ask=input("Show more? 1:Yes 2:No >")
			if ask==1:
				print("     Ver 0.2     ")
				print("Added Verboseness")
				print("and rewrote comm-")
				print("   and system.   ")
				print("=================")
				ask=input("Show more? 1:Yes 2:No >")
				if ask==1:
					print("     Ver 0.1     ")
					print("   OS Created.   ")
					print("=================")
				elif ask==2:
					exit
				else:
					print("Error 04: Invalid answer; exiting app")
			elif ask==2:
				exit
			else:
				print("Error 04: Invalid answer; exiting app")
		else:
			print("Error 04: Invalid answer; exiting app")
	elif command == "ver": # app name: ver
		print "GiraOS/P Version",ver,"Copyright",copyright # print the version - like winver
	elif command == "sudo":
		if sudostatus == 1:
			print("Already superuser; nothing to do")
		else:
			print("Enter your Developer ID for verification.")
			sudoid=input(">")
			if sudoid != checkid:
				print("Error 02: invalid Developer ID")
			else:
				print("You are now a SUPERUSER. You now have priviledges to run superuser apps. Be careful...")
				sudostatus=1
	elif command == "exit":
		sys.exit("exit::user requested exit")
	elif command == "buildtime":
		if sudostatus != 1:
			print("Error 06: not a superuser")
		else:
			print "Built", bd # app name: buildtime
	elif command == "buildcheck":
		if sudostatus != 1:
			print("Error 06: not a superuser")
		else:
			print "GiraOS/P version",buildno # app name: buildcheck
	else:
		print("Error 05: Invalid command") # only applies for numbers (and ver for some reason); text causes a crash
