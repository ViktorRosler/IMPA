import sys, math
from collections import deque

def main():
	# sys.stdin = open('.txt', 'r')

	while True:
		init = sys.stdin.readline().split()

		if init == []:
			break

		a = int(init[0])
		b = int(init[1])

		print(a * b * 2)

			

main()
