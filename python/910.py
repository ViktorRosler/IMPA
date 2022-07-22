import sys

sys.stdin = open("910.txt")

def solve(dp, graph, pos, step):
	if step == 0:
		return graph[pos][2]
	if dp[pos][step] != -1:
		return dp[pos][step]
	dp[pos][step] = solve(dp, graph, graph[pos][0], step -1) + solve(dp, graph, graph[pos][1], step -1)
	return dp[pos][step]

def main():
	for q in range(999999):
		if q > 0:
			sys.stdin.readline()
		a = sys.stdin.readline().strip()

		if a == "":
			break

		n = int(a)
		dp = [[-1 for i in range(50)] for j in range(50)]
		graph = []
		for i in range(n):
			a = sys.stdin.readline().strip().split()
			if a[3] == '-':
				graph.append([ord(a[1])-65, ord(a[2])-65, 0])
			else:
				graph.append([ord(a[1])-65, ord(a[2])-65, 1])
		steps = int(sys.stdin.readline())
		print(solve(dp, graph, 0, steps))

main()