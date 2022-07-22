import sys, math

def main():
	sys.stdin = open('1585.txt', 'r')
	cases = int(sys.stdin.readline())

	for i in range(cases):
		line = sys.stdin.readline()

		summa = 0
		curr = 0

		for j in line:
			if j == "O":
				curr += 1
				summa += curr
			else:
				curr = 0

		print(summa)

main()