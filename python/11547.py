import sys, math

def main():
	#sys.stdin = open('11547.txt', 'r')
	init = int(sys.stdin.readline())
	for i in range(init):
		num = int(sys.stdin.readline())

		num *= 567
		num //= 9
		num += 7492
		num *= 235
		num //= 47
		num -= 498

		s = str(num)[-2]
		print(s)

main()