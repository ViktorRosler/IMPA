import sys, math

def main():
	sys.stdin = open('11854.txt', 'r')

	while True:
		init = sys.stdin.readline().split()

		if init == ['0','0','0']:
			break

		a = int(init[0])
		b = int(init[1])
		c = int(init[2])
		d = max(a,b,c)
		e = min(a,b,c)
		f = a+b+c-d-e

		if e**2 + f**2 == d**2:
			print("right")
		else:
			print("wrong")

main()