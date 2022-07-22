"""
drawers / locked / botom
[i][j][0] = [i-1][j][0] + [i-1][j][1]
[i][j][1] = [i-1][j][0] + [i-1][j-1][1] (or 0)

"""
import sys



sys.stdin = open("11420.txt", 'r')

a = [[[0,0] for i in range(67)] for j in range(67)]
a[1][1][1] = 1
a[1][1][0] = 0
a[1][0][0] = 1
a[1][0][1] = 0
for i in range(2,66):
	for j in range(66):
		a[i][j][0] = a[i-1][j][0] + a[i-1][j][1]
		a[i][j][1] = a[i-1][j][0]
		if j > 0:
			a[i][j][1] += a[i-1][j-1][1]

while True:
	d = sys.stdin.readline().split()
	b = int(d[0])
	c = int(d[1])

	if b < 0 and c < 0:
		break

	if c > b:
		print(0)
	else:
		print(a[b][c][0] + a[b][c][1])

