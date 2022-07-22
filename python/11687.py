import sys, math

def main():
	#sys.stdin = open('11687.txt', 'r')

	while True:
		init = sys.stdin.readline().strip()

		if init == "END":
			break

		#init = int(init)
		l = len(init)
		if init == "1":
			print(1)
		elif l < 2:
			print(2)
		elif l < 10:
			print(3)
		else:
			print(4)

main()