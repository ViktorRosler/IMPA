import sys, math

def main():
	sys.stdin = open('12227.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		init = inp[index].rstrip().split(' ')
		index += 1

main()