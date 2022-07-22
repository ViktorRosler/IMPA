import sys, math

sys.stdin = open("11566.txt")


while True:
	a = sys.stdin.readline().split()

	N,x,T,K = int(a[0]),int(a[1]),int(a[2]),int(a[3])

	# (cost + tea) * 1.1 = x
	# x / 1.1 - tea = cost
	max_cost = math.floor((x * (N+1)) / 1.1 - T * (N + 1))
	# print(max_cost)

	if N == 0:
		break

	items = []
	for i in range(K):
		a = sys.stdin.readline().split()
		items.append((int(a[0]), sum(list(map(int, a[1:])))))

	# dp[K][max_cost][N*2] 
	dp = [[[0 for i in range(2*(N+1)+1)] for j in range(max_cost+1)] for k in range(K+1)]
	# print(dp)
	for i in range(1, K+1):
		for j in range(max_cost+1):
			for k in range(2*(N+1)+1):
				if items[i-1][0] > j:
					dp[i][j][k] = dp[i-1][j][k]
				else:
					dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-items[i-1][0]][k-1] + items[i-1][1])
	print(round(dp[K][max_cost][2*(N+1)] / (N+1), 2))