import sys, itertools

sys.stdin = open("1079.txt", 'r')

case = 0
while True:
	n = int(sys.stdin.readline())

	if n == 0:
		break

	case += 1
	a = []
	for i in range(n):
		b = sys.stdin.readline().split()
		a.append((int(b[0])*60, int(b[1])*60))

	b = list(itertools.permutations(a))

	m = -1
	for i in b:
		low, high = 0, 1440 * 60
		p = 0
		while low < high:
			mid = (low + high) // 2
			if mid == low:
				break
			doable = True
			current = 0
			for j in range(len(i)):
				if j == 0:
					current = i[j][0]
				elif j == len(i) - 1:
					if current + mid <= i[j][1]:
						break
					doable = False
				else:
					if i[j][0] > current + mid:
						current = i[j][0]
					elif i[j][1] >= current + mid:
						current += mid
					else:
						doable = False
						break
			if doable:
				low = mid
			else:
				high = mid
		m = max(m, low)
		e = m % 60
		if e < 10:
			e = "0" + str(e)
	print("Case {0}: {1}:{2}".format(case, m // 60, str(e)))