import sys, math

def main():
	sys.stdin = open('10929.txt', 'r')

	while True:
		init = sys.stdin.readline().strip()

		if init == "0":
			break

		if int(init) % 11 == 0:
			print("{0} is a multiple of 11.".format(init))
		else:
			print("{0} is not a multiple of 11.".format(init))

main()