import sys, math

sys.stdin = open("1347.txt")

def dp_func(a,b,dp,dist,p):
	if dp[a][b] != -1:
		return dp[a][b]
	if a == p-1:
		c = dist[b][p-1]
		dp[a][b] = c
		dp[b][a] = c
		return c
	c = min(dp_func(a+1,b,dp,dist,p) + dist[a][a+1], dp_func(a+1,a,dp,dist,p) + dist[b][a+1])
	dp[a][b] = c
	dp[b][a] = c
	return c

while True:
	p = sys.stdin.readline()

	if p == "":
		break

	if p.strip() == "":
		continue

	p = int(p)
	if p == 0:
		print("0.00")
		continue

	dp = [[-1 for i in range(p+10)] for j in range(p+10)]
	dist = [[0 for i in range(p+10)] for j in range(p+10)]

	a = []
	c = 0
	while c < p:
		b = sys.stdin.readline().split()
		if b == []:
			continue
		c += 1
		a.append((int(b[0]), int(b[1])))

	for i in range(p-1):
		for j in range(i+1, p):
			dist[i][j] = math.sqrt((a[i][0] - a[j][0])**2 + (a[i][1] - a[j][1])**2)

	b = dp_func(0,0,dp,dist,p)
	print("{:.2f}".format(b))