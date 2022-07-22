import sys, math

def main():
	sys.stdin = open('11518.txt', 'r')

	cases = int(sys.stdin.readline())

	for i in range(cases):
		init = sys.stdin.readline().split()

		tiles = int(init[0])
		m = int(init[1])
		l = int(init[2])

		dic = {}
		done = set()
		todo = set()
		for j in range(m):
			init = sys.stdin.readline().split()

			if init[0] not in dic:
				dic[init[0]] = []

			dic[init[0]].append(init[1])

		for j in range(l):
			init = sys.stdin.readline().strip()
			todo.add(init)

		while len(todo) > 0:
			s = todo.pop()
			done.add(s)
			if str(s) in dic:
				for k in dic[s]:
					if k not in done:
						todo.add(k)

		print(len(done))

main()