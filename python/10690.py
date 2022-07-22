import sys, random, itertools


sys.stdin = open('10690.txt', 'r')

while True:
	a = sys.stdin.readline().split()

	if not a:
		break

	n = int(a[0])
	m = int(a[1])

	a = sys.stdin.readline().split()
	a = list(map(int, a))
	s = sum(a)

	c = min(n,m)

	d = []
	e = []
	todo = len(a)
	mini = 999999
	maxi = -999999

	dp = {}
	for i in range(51):
		for j in range(5001):
			dp[(i,j)] = 0

	for i in range(len(a)):
		l = []
		for j in range(min(i+1, 50)):

			for k in range(5001):
				if dp[(j,k)] == 1:
					l.append((j+1, k+a[i]))
		for j in l:
			dp[(j[0], j[1])] = 1

	print("asdf")