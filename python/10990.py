import sys

def calc():
	for i in range(2, limit):
		if phi[i] == 0:
			phi[i] = i-1
			for j in range(i+i, limit, i):
				if phi[j] == 0:
					phi[j] = j
				phi[j] -= phi[j] // i

sys.stdin = open("10990.txt")

limit = 2000005
dp = [0 for i in range(limit)]
dp[1] = dp[2] = 1
phi = [0 for i in range(limit)]
phi[1] = 1

calc()

for i in range(3, limit):
	dp[i] = dp[phi[i]] + 1


for i in range(1,limit):
	dp[i] += dp[i-1]


cases = int(sys.stdin.readline())
for i in range(cases):
	a = sys.stdin.readline().strip().split()
	print(dp[int(a[1])] - dp[int(a[0])-1])


