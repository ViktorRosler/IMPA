import sys

sys.stdin = open("11805.txt", 'r')

cases = int(sys.stdin.readline())

for i in range(cases):
	a = sys.stdin.readline().split()

	players = int(a[0])
	current = int(a[1])
	passes = int(a[2])

	for j in range(passes):
		current += 1
		if current > players:
			current = 1

	print("Case {0}: {1}".format(i+1, current))