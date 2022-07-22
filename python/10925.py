import sys, math

def main():
	sys.stdin = open('10925.txt', 'r')
	index = 0

	while True:
		index += 1
		init = sys.stdin.readline().split()

		items = int(init[0])
		friends = int(init[1])

		if items == 0:
			break

		summa = 0
		for i in range(items):
			summa += int(sys.stdin.readline())

		print("Bill #{0} costs {1}: each friend should pay {2}\n".format(index,summa,summa//friends))



			

main()