import sys, math

def main():
	# sys.stdin = open('10297.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while True:
		init = inp[index].rstrip().split(' ')
		index += 1
		D = int(init[0])
		V = int(init[1])

		if D == 0:
			break

		A = 2/3 * (D/2)**2 * math.pi * D - V
		d = (A * 6 / math.pi) ** (1./3)
		print('{:.3f}'.format(d))

main()