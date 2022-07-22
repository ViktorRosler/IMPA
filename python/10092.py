import sys, math
from collections import deque
from random import *

def main():
	sys.stdin = open('10092.txt', 'r')

	while True:
		init = sys.stdin.readline().split()

		if init == ['0', '0']:
			break

		nk = int(init[0])
		np = int(init[1])

		cat = {}
		todo = {}
		for i in range(1, nk+1):
			cat[i] = set()
			todo[i] = set()

		cat_size = []
		init = sys.stdin.readline().split()
		for i in range(nk):
			cat_size.append(int(init[i]))

		
		for i in range(1, np+1):
			init = sys.stdin.readline().split()
			if init[0] == '1':
				cat[int(init[1])].add(i)
			else:
				for j in range(1, len(init)):
					todo[int(init[j])].add(i)

		done = False
		go_on = True
		while not done:
			done = True
			go_on = False

			for i in range(1, nk+1):
				if len(cat[i]) < cat_size[i-1]:
					done = False
					break


			if go_on == False:
				break

			

main()