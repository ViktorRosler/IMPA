import sys, math
from collections import deque

def pr(n ,k, choice):
	if n == 0 and k == 0:
		return
	pr(choice[n][k][0] - 1, k - 1, choice)

	if choice[n][k][0] == n:
		print("Depot", k, "at restaurant", choice[n][k][1], "serves restaurant", n)
	else:
		print("Depot", k, "at restaurant", choice[n][k][1], "serves restaurants", choice[n][k][0], "to", n)

def cost(i, j, summa, pos):
	c = (i + j) // 2
	return (pos[c] * (2 * c - i - j) - (summa[c-1] - summa[i-1]) + (summa[j] - summa[c]), c)

def solve(n,k, summa, pos, choice):
	dp = [[999999999 for i in range(205)] for j in range(35)]
	dp[0][0] = 0
	for i in range(1, n+1):
		for j in range(1, min(k,i) + 1):
			m = j
			while (m <= i):
				(co, c) = cost(m, i, summa, pos)
				val = dp[m-1][j-1] + co
				if val < dp[i][j]:
					choice[i][j] = (m, c)
					dp[i][j] = val
				m += 1
	pr(n, k, choice)
	print("Total distance sum =", dp[n][k])	
	print()			

def main():
	sys.stdin = open('662.txt', 'r')

	summa = [0 for i in range(205)]
	pos = [0 for i in range(205)]
	choice = [[(0,0) for i in range(205)] for j in range(35)]

	chain = 1
	while True:
		init = sys.stdin.readline().split()
		n = int(init[0])
		k = int(init[1])
		if n == 0 and k == 0:
			return
		for i in range(1, n+1):
			pos[i] = int(sys.stdin.readline())
			summa[i] = (pos[i] + summa[i-1])
		print("Chain", chain)
		chain += 1
		solve(n,k, summa, pos, choice)

			

main()