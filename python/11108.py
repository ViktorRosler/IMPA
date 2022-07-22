import sys, math

def eval(WFF):
	index = len(WFF) - 1

	while (index > 0):
		index2 = index
		while WFF[index2].isdigit():
			index2 -= 1

		a = WFF[index2]

		b = WFF[index2 + 1]

		if a == "N":
			if b == "1":
				WFF = WFF[:index2] + "0" + WFF[index2 + 2:]
			elif b == "0":
				WFF = WFF[:index2] + "1" + WFF[index2 + 2:]
			index -= 1
			continue

		c = WFF[index2 + 2]
		index -= 2

		if a == "K":
			if b == "1" and c == "1":
				WFF = WFF[:index2] + "1" + WFF[index2 + 3:]
			else:
				WFF = WFF[:index2] + "0" + WFF[index2 + 3:]
		elif a == "A":
			if b == "1" or c == "1":
				WFF = WFF[:index2] + "1" + WFF[index2 + 3:]
			else:
				WFF = WFF[:index2] + "0" + WFF[index2 + 3:]
		elif a == "C":
			if b == "1" and c == "0":
				WFF = WFF[:index2] + "0" + WFF[index2 + 3:]
			else:
				WFF = WFF[:index2] + "1" + WFF[index2 + 3:] 
		elif a == "E":
			if b == c:
				WFF = WFF[:index2] + "1" + WFF[index2 + 3:]
			else:
				WFF = WFF[:index2] + "0" + WFF[index2 + 3:] 

	if WFF[0] == "1": 
		return True
	else:
		return False



def main():
	#sys.stdin = open('11108.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		init = inp[index].rstrip()
		index += 1

		if init == '0':
			return

		tautology = True
		for i in range(32):
			copy = init[:]

			if i >= 16:
				copy = copy.replace("p", "1")
				i -= 16
			else:
				copy = copy.replace("p", "0")

			if i >= 8:
				copy = copy.replace("q", "1")
				i -= 8
			else:
				copy = copy.replace("q", "0")	

			if i >= 4:
				copy = copy.replace("r", "1")
				i -= 4
			else:
				copy = copy.replace("r", "0")

			if i >= 2:
				copy = copy.replace("s", "1")
				i -= 2
			else:
				copy = copy.replace("s", "0")

			if i >= 1:
				copy = copy.replace("t", "1")
			else:
				copy = copy.replace("t", "0")

			tautology = eval(copy)
			if not tautology:
				break

		if tautology:
			print("tautology")
		else:
			print("not")


main()