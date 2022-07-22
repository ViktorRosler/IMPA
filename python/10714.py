import sys, math

def main():
	#sys.stdin = open('10714.txt', 'r')

	cases =  int(sys.stdin.readline())

	index = 0
	while index < cases:
		index += 1
		init = sys.stdin.readline().split()
		pole_len = int(init[0])
		nr_ants = int(init[1])

		init = []
		while len(init) < nr_ants:
			c = sys.stdin.readline().split()
			for i in c:
				init.append(int(i))

		least = 0
		maxi = 0
		for i in range(len(init)):
			a = min(int(init[i]), pole_len - int(init[i]))
			b = max(int(init[i]), pole_len - int(init[i]))
			least = max(a, least)
			maxi = max(b, maxi)
		print(least, maxi)

main()