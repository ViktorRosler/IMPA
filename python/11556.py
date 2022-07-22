import sys, math

# 0bit - 1 alternativ
# 1bit - 2 alternativ
# 2bit - 4 alternativ
# 3bit - 8 alternativ
# totalt 2**(b+1) -1 alternativ

def main():
	# sys.stdin = open('11556.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		init = inp[index].rstrip().split()
		index += 1

		N = int(init[0])
		b = int(init[1])

		if N > (2)**(b+1) - 1:
			print('no')
		else:
			print('yes')

main()