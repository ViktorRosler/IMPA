import sys, math
from collections import deque

a = 2000000000
l = []

def rec(c, n):
	n = n*c
	if n > a:
		return
	l.append(n)
	if c <= 2:	
		rec(2, n)
		rec(3, n)
		rec(5, n)
		rec(7, n)
	if c == 3:
		rec(3, n)
		rec(5, n)
		rec(7, n)
	if c == 5:
		rec(5, n)
		rec(7, n)
	if c == 7:
		rec(7, n)

def main():
	#sys.stdin = open('443.txt', 'r')

	rec(1, 1)
	l.sort()
	
	while True:
		init = int(sys.stdin.readline())

		if init == 0:
			break

		b = l[init-1]

		if init % 10 == 1 and init % 100 != 11:
			print("The {0}st humble number is {1}.".format(init, b))
		elif init % 10 == 2 and init % 100 != 12:
			print("The {0}nd humble number is {1}.".format(init, b))
		elif init % 10 == 3 and init % 100 != 13:
			print("The {0}rd humble number is {1}.".format(init, b))
		else:
			print("The {0}th humble number is {1}.".format(init,b))

main()