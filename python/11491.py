import sys, math
from collections import deque

def main():
	sys.stdin = open('11491.txt', 'r')

	while True:
		init = sys.stdin.readline().split()

		N = int(init[0])
		D = int(init[1])

		if (N == 0 and D == 0):
			break

		line = sys.stdin.readline().strip()
		line = deque(line)

		i = 0
		while (i < len(line)-1 and D > 0):
			if int(line[i]) < int(line[i+1]):
				line.remove(line[i])
				D -= 1
				if i > 0:
					i -= 1
			else:
				i += 1

		for j in range(10):
			i = 0
			while (i < len(line) and D > 0):
				if int(line[i]) == j:
					line.remove(line[i])
					D-= 1
				else:
					i += 1

			if D == 0:
				break

		print("".join(line))

main()