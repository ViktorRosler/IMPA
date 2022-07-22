import sys, math

def main():
	# sys.stdin = open('847.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		init = int(inp[index].rstrip())
		index += 1

		num = 1
		while True:
			if num * 9 >= init:
				print('Stan wins.')
				break
			else:
				num *= 2

			if num * 9 >= init:
				print('Ollie wins.')
				break
			else:
				num *= 9

main()