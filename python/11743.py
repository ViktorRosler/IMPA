import sys, math

def main():
	sys.stdin = open('11743.txt', 'r')

	cases = int(sys.stdin.readline())

	for i in range(cases):
		init = sys.stdin.readline().rstrip()

		a = 0

		s = str(int(init[0])*2) 
		a += int(s[0])
		if len(s) == 2:
			a += int(s[1])

		s = str(int(init[2])*2) 
		a += int(s[0])
		if len(s) == 2:
			a += int(s[1])

		s = str(int(init[5])*2) 
		a += int(s[0])
		if len(s) == 2:
			a += int(s[1])

		s = str(int(init[7])*2) 
		a += int(s[0])
		if len(s) == 2:
			a += int(s[1])

		s = str(int(init[10])*2) 
		a += int(s[0])
		if len(s) == 2:
			a += int(s[1])

		s = str(int(init[12])*2) 
		a += int(s[0])
		if len(s) == 2:
			a += int(s[1])

		s = str(int(init[15])*2) 
		a += int(s[0])
		if len(s) == 2:
			a += int(s[1])

		s = str(int(init[17])*2) 
		a += int(s[0])
		if len(s) == 2:
			a += int(s[1])


		a += int(init[1]) + int(init[3]) + int(init[6]) + int(init[8]) \
		  + int(init[11]) + int(init[13]) + int(init[16]) + int(init[18])

		if str(a)[-1] == '0':
			print("Valid")
		else:
			print("Invalid")
		 

		

main()