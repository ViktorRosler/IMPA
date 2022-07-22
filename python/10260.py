import sys, math

def main():
	#sys.stdin = open('10260.txt', 'r')

	while True:
		init = sys.stdin.readline()
		curr = ""

		if init == "":
			break

		out = ""

		for char in init:
			if char == "B" or char == "F" or char == "P" or char == "V":
				if curr != "1":
					out += "1"
					curr = "1"
			elif char == "C" or char == "G" or char == "J" or char == "K" or char == "Q" \
			or char == "S" or char == "X" or char == "Z":
				if len(out) == 0 or curr != "2":
					out += "2"
					curr = "2"
			elif char == "D" or char == "T":
				if curr != "3":
					out += "3"
					curr = "3"
			elif char == "L":
				if curr != "4":
					out += "4"
					curr = "4"
			elif char == "M" or char == "N":
				if curr != "5":
					out += "5"
					curr = "5"
			elif char == "R":
				if curr != "6":
					out += "6"
					curr = "6"
			else:
				curr = ""									 		
		print(out)


main()