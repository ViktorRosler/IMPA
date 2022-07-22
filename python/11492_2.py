import sys
from queue import PriorityQueue

def djikstra(g, start_lang, end_lang):
	pq = PriorityQueue()
	pq.put((0, 'A', start_lang))

	while not pq.empty():
		p = pq.get()

		if p[2] == end_lang:
			return p[0]

		for i in range(len(g[p[2]])):
			if (not g[p[2]][i][2]) and (g[p[2]][i][1][0] != p[1]):
				pq.put([p[0] + len(g[p[2]][i][1]), g[p[2]][i][1][0], g[p[2]][i][0]])
				g[p[2]][i][2] = True

	return -1


sys.stdin = open("11492.txt")

while True:
	M = int(sys.stdin.readline())

	# print(M)

	if M == 0:
		break

	a = sys.stdin.readline().strip().split()
	start = a[0]
	end = a[1]

	m = {}
	graph = []
	graph_index = 0

	for i in range(M):
		abw = sys.stdin.readline().strip().split()
		a = abw[0]
		b = abw[1]
		w = abw[2]

		if a not in m:
			m[a] = graph_index
			graph_index += 1
			graph.append([])

		if b not in m:
			m[b] = graph_index
			graph_index += 1
			graph.append([])

		graph[m[a]].append([m[b], w, False])
		graph[m[b]].append([m[a], w, False])

	if (start not in m) or (end not in m):
		print("impossivel")
	else:
		cost = djikstra(graph, m[start], m[end])
		if cost >= 0:
			print(cost)
		else:
			print("impossivel")

	





