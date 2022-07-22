import sys

sys.stdin = open("607.txt")

def val(v, C):
	if v == 0:
		return 0
	if v <= 10:
		return -C
	return (v - 10)**2

def solve(n, L, C, t):
	sum = [0 for i in range(1011)]
	for i in range(1, n+1):
		sum[i] = sum[i-1] + t[i]

	trail = 0
	cnt = 1
	low = [0 for i in range(1011)]
	for i in range(1, n+1):
		trail += t[i]
		if trail > L:
			trail = t[i]
			cnt += 1
		low[i] = cnt

	trail = 0
	high = [0 for i in range(1011)]
	for i in range(n, 0, -1):
		trail += t[i]
		if trail > L:
			trail = t[i]
			cnt -= 1
		high[i] = cnt

	dp = [[999999999 for i in range(1011)] for j in range(1011)]
	dp[0][0] = 0
	for k in range(1, n+1):
		for i in range(low[k], high[k]+1):
			for j in range(k-1, -1, -1):
				v = L - (sum[k] - sum[j])
				if v >= 0:
					dp[i][k] = min(dp[i][k], dp[i-1][j] + val(v, C))
				else:
					break
	print("Minimum number of lectures: {0}".format(low[n]))
	print("Total dissatisfaction index: {0}".format(dp[low[n]][n]))

def main():
	for case in range(1, 9999):
		n = int(sys.stdin.readline())

		if n == 0:
			break

		a = sys.stdin.readline().strip().split()
		L = int(a[0])
		C = int(a[1])

		t = [0 for i in range(1011)]

		for i in range(1, n+1):
			t[i] = int(sys.stdin.readline())

		if case > 1:
			print()
		print("Case {0}:".format(case))
		solve(n, L, C, t) 

main()