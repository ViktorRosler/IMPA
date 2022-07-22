import sys

dp = {}
first = True

def calc(obj, min_x, max_x, min_y, max_y, min_z, max_z):
	if first:
		first = False
		for j in range(int(a[0])):
			for k in range(int(a[1])):
				for l in range(int(a[2])):
	else:




sys.stdin = open("10755.txt")

cases = int(sys.stdin.readline())

for i in range(cases):
	sys.stdin.readline()

	dp = {}
	a = sys.stdin.readline().strip().split()
	b = sys.stdin.readline().strip().split()
	obj = {}
	
	for j in range(int(a[0])):
		for k in range(int(a[1])):
			for l in range(int(a[2])):
				obj[(j,k,l)] = int(b[x])
				x += 1

	x = -999999999999999
	for j in range(int(a[0])):
		for k in range(int(a[1])):
			for l in range(int(a[2])):
				obj[(j,k,l)] = int(b[x])
				x = max(x, calc(obj, j, int(a[0]), k, int(a[1]), l, int(a[2])))		

	if i > 0:
		print()
	print(x)