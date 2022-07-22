import sys

sys.stdin = open("872.txt")
cases = int(sys.stdin.readline())
for i in range(cases):
	sys.stdin.readline()
	a = sys.stdin.readline().strip().split()
	a.sort()
	b = [a.copy() for j in range(len(a))]
	c = sys.stdin.readline().strip().split()
	for j in c:
		for l in range(len(b)):
			if j[0] in b[l] and j[2] not in b[l]:
				break
			elif j[0] not in b[l] and j[2] in b[l]:
				b[l].remove(j[2])
			elif j[0] in b[l] and j[2] in b[l]:
				b[l].remove(j[2])
				break
	# print(b)
	asdf = [[q] for q in b[0]]
	for j in range(1, len(b)):
		n = []
		for k in asdf:
			for l in b[j]:
				if l not in k:
					for m in c:
						if m[2] == l and m[0] not in k:
							break
					else:
						n.append(k + [l])
		asdf = n
	if i > 0:
		print()
	if len(asdf) > 0:
		for j in asdf:
			s = j[0]
			for k in range(1, len(j)):
				s += " " + j[k]
			print(s)
	else:
		print("NO")
