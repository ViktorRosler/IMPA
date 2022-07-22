import sys, math

def main():
	# sys.stdin = open('10220.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		num = int(inp[index].rstrip())
		index += 1

		fac = 1
		for i in range(2,num+1):
			fac *= i

		s = str(fac)
		sum = 0
		for c in s:
			sum += int(c)

		print(sum)


main()