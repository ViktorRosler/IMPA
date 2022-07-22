import sys, math


dp = {}

def fib(n):
	if n == 0:
		return 1

	if n == 1:
		return 2

	if n not in dp:
		dp[n] = fib(n-1) + fib(n-2)

	return dp[n]

def main():
	sys.stdin = open('10334.txt', 'r')

	while True:
		init = sys.stdin.readline()

		if init == "":
			break

		print(fib(int(init)))

main()