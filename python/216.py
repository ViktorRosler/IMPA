import sys, itertools, math

sys.stdin = open("216.txt")

for i in range(1, 999999):
	a = sys.stdin.readline().strip()

	if a == "0":
		break

	l = []
	for j in range(int(a)):
		b = sys.stdin.readline().split()
		l.append((int(b[0]), int(b[1])))

	n = 999999
	m = []
	for j in list(itertools.permutations(l)):
		s = 0
		for k in range(len(j)-1):
			s += math.hypot(j[k+1][0] - j[k][0], j[k+1][1] - j[k][1]) + 16
		if s < n:
			n = s
			m = list(j)
	print("**********************************************************")
	print("Network #{0}".format(i))
	for j in range(len(m)-1):
		s = math.hypot(m[j+1][0] - m[j][0], m[j+1][1] - m[j][1]) + 16
		print("Cable requirement to connect ({0},{1}) to ({2},{3}) is {4:.2f} feet.".format(m[j][0], m[j][1], m[j+1][0], m[j+1][1], s))
	print("Number of feet of cable required is {0:.2f}.".format(round(n,2)))