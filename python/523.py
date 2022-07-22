import sys

sys.stdin = open("523.txt")

cases = int(sys.stdin.readline())
sys.stdin.readline()

for i in range(cases):
	if i > 0:
		print()
	matrix = []
	a = sys.stdin.readline().strip().split()
	n = len(a)
	matrix.append([])
	for j in a:
		if j == "-1":
			matrix[0].append(999999999)
		else:
			matrix[0].append(int(j))
	for j in range(1,n):
		matrix.append([])
		a = sys.stdin.readline().strip().split()
		for k in a:
			if k == "-1":
				matrix[j].append(999999999)
			else:
				matrix[j].append(int(k))
	taxes = []
	a = sys.stdin.readline().strip().split()
	for j in a:
		taxes.append(int(j))
	nexts = [[j for j in range(n)] for k in range(n)]
	for u in range(n):
		for s in range(n):
			if matrix[s][u] != 999999999:
				for t in range(n):
					if matrix[u][t] != 999999999 and matrix[s][t] > matrix[s][u] + taxes[u] + matrix[u][t]:
						matrix[s][t] = matrix[s][u] + taxes[u] + matrix[u][t]
						nexts[s][t] = nexts[s][u]
	printed = False
	while True:
		a = sys.stdin.readline().strip().split()
		if a == []:
			break

		if printed:
			print()
		else:
			printed = True

		print("From {0} to {1} :".format(a[0], a[1]))
		s = int(a[0]) - 1
		e = int(a[1]) - 1
		print("Path: {0}".format(s+1), end="")
		if s != e:
			u = s
			while u != e:
				u = nexts[u][e]
				print("-->{0}".format(u+1), end="")
		print()
		print("Total cost : {0}".format(matrix[s][e]))
