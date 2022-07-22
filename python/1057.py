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

	g1 = [[] for j in range(N)]
	g2 = [[] for j in range(N)]

	dist = [[INF for i in range(N)] for j in range(N)]

	for i in range(1, paths+1):
		a = sys.stdin.readline().split()
		s, t = int(a[0]), int(a[1])
		dist[s][t] = 1
		g1[s].append(t)
		g2[t].append(s)


	for i in range(1, nodes+1):
		for j in range(1, nodes+1):
			for k in range(1, nodes+1):
				dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
	print("Network {0}".format(w))
	if dist[1][2] != INF and dist[2][1] != INF:
		""
	else:
		print("Impossible")