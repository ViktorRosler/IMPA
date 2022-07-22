import sys, math

def main():
	# sys.stdin = open('13161.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		D = int(inp[index].rstrip())
		R = int(inp[index+1].rstrip())
		T = int(inp[index+2].rstrip())
		index += 3

		candles = R + T
		rita_age = D
		theo_age = 0

		rita_can = 0

		while D >= 4:
			rita_can += D
			D -= 1
		theo_can = 0

		while rita_can + theo_can < candles:
			rita_age += 1
			theo_age += 1

			if rita_age >= 4:
				rita_can += rita_age

			if theo_age >= 3:
				theo_can += theo_age

		ans = R - rita_can
		print(ans)



main()