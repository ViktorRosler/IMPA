import sys, math

def fact(num):
	fac = 1
	for i in range(1,num+1):
		fac *= i
	return fac

def main():
	# sys.stdin = open('911.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		n = int(inp[index].rstrip())
		index += 2

		coeff = inp[index].rstrip().split(' ')
		index += 1

		ans = fact(n)
		for i in coeff:
			ans /= fact(int(i))

		print(int(ans))

main()