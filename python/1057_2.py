import sys

sys.stdin = open("1057.txt")

N, INF = 105, 999999

for w in range(1, INF):
	a = sys.stdin.readline().split()
	print(a)

	if a[0] == "0" and a[1] == "0":
		break

	nodes = int(a[0])
	paths = int(a[1])

	dist = [[INF for i in range(N)] for j in range(N)]

	for i in range(1, nodes+1):
		if i == 1 or i == 2:
			dist[i][i] = 1
		else:
			dist[i][i] = 0

	p_dict = {}
	for i in range(1, paths+1):
		a = sys.stdin.readline().split()
		s, t = int(a[0]), int(a[1])
		dist[s][t] = 0
		p_dict[(s,t)] = True

	for i in range(1, nodes+1):
		for j in range(1, nodes+1):
			for k in range(1, nodes+1):
				dist[j][k] = min(dist[j][k], dist[j][j] + dist[j][i] + dist[i][k] + dist[k][k])


	if dist[1][2] != INF and dist[2][1] != INF:
		print(dist[1][2], dist[2][1])
	else:
		print("Impossible")