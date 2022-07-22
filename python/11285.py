import sys

sys.stdin = open("11285.txt")


while True:
	n = int(sys.stdin.readline())

	if n == 0:
		break

	a = float(sys.stdin.readline())

	high_can = 1000
	high_us = int((high_can / a) * 0.97 * 100) / 100


	for i in range(1,n):
		a = float(sys.stdin.readline())
		old = high_us
		new = int((high_can / a) * 0.97 * 100) / 100
		high_us = max(high_us, new)
		new = int(old * a * 0.97 * 100) / 100
		high_can = max(high_can, new)

	print("{:.2f}".format(high_can))