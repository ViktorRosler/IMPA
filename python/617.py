import sys

sys.stdin = open("617.txt")

i = 0
while True:
	a = sys.stdin.readline().strip()

	if a == "":
		continue

	i += 1

	a = int(a)

	if a == -1:
		break

	lights = []
	for j in range(a):
		b = sys.stdin.readline().split()
		lights.append((float(b[0]), int(b[1]) + int(b[2]), int(b[3])))

	ranges = [[]]
	for j in range(30, 61):
		for k in lights:
			t = (k[0]*3600)/ j 
			s = 0
			u = True
			v = 0
			while s < t:
				if v % 2 == 0:
					s += k[1]
				else:
					s += k[2]
					if s > t:
						u = False
				v += 1
			if not u:
				break
		else:
			if len(ranges[-1]) == 0:
				ranges[-1].append(j)
			elif len(ranges[-1]) == 1 and ranges[-1][0] == j - 1:
				ranges[-1].append(j)
			elif len(ranges[-1]) == 2 and ranges[-1][1] == j - 1:
				ranges[-1][1] = j
			else:
				ranges.append([j])
	s = "Case " + str(i) + ": "
	if ranges == [[]]:
		s += "No acceptable speeds."
	else:
		for j in range(len(ranges)):
			if j > 0:
				s += ", "
			s += str(ranges[j][0])
			if len(ranges[j]) == 2:
				s += "-" + str(ranges[j][1])


	print(s)
