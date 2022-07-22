import sys, math
from collections import deque

def main():
	#sys.stdin = open('11283.txt', 'r')

	cases = int(sys.stdin.readline())

	con = {}
	con[0] = [1,4,5]
	con[1] = [0,2,4,5,6]
	con[2] = [1,3,5,6,7]
	con[3] = [2,6,7]
	con[4] = [0,1,5,8,9]	
	con[5] = [0,1,2,4,6,8,9,10]
	con[6] = [1,2,3,5,7,9,10,11]
	con[7] = [2,3,6,10,11]
	con[8] = [4,5,9,12,13]
	con[9] = [4,5,6,8,10,12,13,14]
	con[10] = [5,6,7,9,11,13,14,15]
	con[11] = [6,7,10,14,15]
	con[12] = [8,9,13]
	con[13] = [8,9,10,12,14]
	con[14] = [9,10,11,13,15]
	con[15] = [10,11,14]

	for i in range(cases):
		sys.stdin.readline()

		points = 0
		board = {}
		for j in range(4):
			a = sys.stdin.readline().strip()
			for k in range(4):
				board[j*4 + k] = a[k]

		words = int(sys.stdin.readline())

		for j in range(words):
			word = sys.stdin.readline().strip()
			chains = []
			for key,value in board.items():
				if word[0] == value:
					chains.append([key])
			for k in range(1,len(word)):
				new = []
				for l in range(len(chains)):
					for m in con[chains[l][-1]]:
						if board[m] == word[k] and m not in chains[l]:
							new.append(chains[l] + [m])
				chains = new
			if len(chains) > 0:
				#print(chains)
				b = len(word)
				if b <= 4:
					points += 1
				elif b == 5:
					points += 2
				elif b == 6:
					points += 3
				elif b == 7:
					points += 5
				else:
					points += 11

		print("Score for Boggle game #{0}: {1}".format(i+1, points))

main()