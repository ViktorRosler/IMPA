import sys, math

def main():
	#sys.stdin = open('11462.txt', 'r')

	while True:
		init = int(sys.stdin.readline())

		if init == 0:
			break

		init = sys.stdin.readline().split()

		tal = [0] * 100
		for i in init:
			tal[int(i)-1] += 1

		first = True
		for i in range(1, len(tal)+1):
			for j in range(tal[i-1]):
				if first:
					print(i, end='')
					first = not first
				else:
					print('', i, end='')
		print()

main()