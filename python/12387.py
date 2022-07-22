import sys

sys.stdin = open("12387.txt")

while True:
	a = sys.stdin.readline().strip().split()
	S = int(a[0])
	P = int(a[1])

	if S == -1:
		break

	pieces = []
	for i in range(P):
		pieces.append(int(sys.stdin.readline()))

	sym = []
	for i in range(len(pieces)-1):
		a = pieces[i+1] - pieces[0]
		for j in range(1,len(pieces)):
			if (pieces[j] + a) % 360_000 != pieces[(j+i+1) % len(pieces)]:
				break
		else:
			sym.append(a)

	rotations = [P]
	for i in range(len(sym)):
		for j in range(2, 360_005):
			if (pieces[0] + sym[i]*j) % 360_000 == pieces[0]:
				rotations.append(P // j)
				break
	s = 0
	for i in rotations:
		s += S**i

	print((s // len(rotations)) % 100_000_007)

	sys.stdin.readline()
