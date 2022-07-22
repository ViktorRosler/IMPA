import sys, math
from collections import deque

def main():
	# sys.stdin = open('.txt', 'r')

	dp = [1,2,2]
	for i in range(3,80):
		dp.append(dp[i-2] + dp[i-3])

	while True:
		init = sys.stdin.readline()

		if init == "":
			break

		init = int(init)

		print(dp[init-1])

			

main()