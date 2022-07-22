import sys, math
from collections import deque

def main():
	sys.stdin = open('8_1.txt', 'r')

	while True:
		inp = sys.stdin.readline().split()

		N = int(inp[0])
		M = int(inp[1])

		if N == 0 and M == 0:
			return

		dic = {}

		total = 0
		for i in range(N+M):
			a = int(sys.stdin.readline())
			if a in dic:
				total += 1
			else:
				dic[a] = 1

		print(total)
			

main()