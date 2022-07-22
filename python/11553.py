import sys, math
from collections import deque

def main():
	#sys.stdin = open('11553.txt', 'r')

	cases = int(sys.stdin.readline())

	for i in range(cases):
		n = int(sys.stdin.readline())

		board = []
		for i in range(n):
			board.append([])
			b = sys.stdin.readline().split()
			for j in b:
				board[-1].append(int(j))

		

		mini = 999999999
		if n == 8:
			for i1 in range(8):
				for i2 in range(8):
					if (i2 == i1):
						continue
					for i3 in range(8):
						if (i3 == i2 or i3 == i1):
							continue
						for i4 in range(8):
							if (i4 == i3 or i4 == i2 or i4 == i1):
								continue
							for i5 in range(8):
								if (i5 == i4 or i5 == i3 or i5 == i2 or i5 == i1):
									continue
								for i6 in range(8):
									if (i6 == i5 or i6 == i4 or i6 == i3 or i6 == i2 or i6 == i1):
										continue
									for i7 in range(8):
										if (i7 == i6 or i7 == i5 or i7 == i4 or i7 == i3 or i7 == i2 or i7 == i1):
											continue
										for i8 in range(8):
											if (i8 == i7 or i8 == i6 or i8 == i5 or i8 == i4 or i8 == i3 or i8 == i2 or i8 == i1):
												continue
											a = board[0][i1] + board[1][i2] + board[2][i3] + board[3][i4] 
											a += board[4][i5] + board[5][i6] + board[6][i7] + board[7][i8]
											mini = min(a, mini)
		elif n == 7:
			for i1 in range(7):
				for i2 in range(7):
					if (i2 == i1):
						continue
					for i3 in range(7):
						if (i3 == i2 or i3 == i1):
							continue
						for i4 in range(7):
							if (i4 == i3 or i4 == i2 or i4 == i1):
								continue
							for i5 in range(7):
								if (i5 == i4 or i5 == i3 or i5 == i2 or i5 == i1):
									continue
								for i6 in range(7):
									if (i6 == i5 or i6 == i4 or i6 == i3 or i6 == i2 or i6 == i1):
										continue
									for i7 in range(7):
										if (i7 == i6 or i7 == i5 or i7 == i4 or i7 == i3 or i7 == i2 or i7 == i1):
											continue
										a = board[0][i1] + board[1][i2] + board[2][i3] + board[3][i4] 
										a += board[4][i5] + board[5][i6] + board[6][i7]
										mini = min(a, mini)
		elif n == 6:
			for i1 in range(6):
				for i2 in range(6):
					if (i2 == i1):
						continue
					for i3 in range(6):
						if (i3 == i2 or i3 == i1):
							continue
						for i4 in range(6):
							if (i4 == i3 or i4 == i2 or i4 == i1):
								continue
							for i5 in range(6):
								if (i5 == i4 or i5 == i3 or i5 == i2 or i5 == i1):
									continue
								for i6 in range(6):
									if (i6 == i5 or i6 == i4 or i6 == i3 or i6 == i2 or i6 == i1):
										continue
									a = board[0][i1] + board[1][i2] + board[2][i3] + board[3][i4] 
									a += board[4][i5] + board[5][i6]
									mini = min(a, mini)
		elif n == 5:
			for i1 in range(5):
				for i2 in range(5):
					if (i2 == i1):
						continue
					for i3 in range(5):
						if (i3 == i2 or i3 == i1):
							continue
						for i4 in range(5):
							if (i4 == i3 or i4 == i2 or i4 == i1):
								continue
							for i5 in range(5):
								if (i5 == i4 or i5 == i3 or i5 == i2 or i5 == i1):
									continue
								a = board[0][i1] + board[1][i2] + board[2][i3] + board[3][i4] + board[4][i5]
								mini = min(a, mini) 
		elif n == 4:
			for i1 in range(4):
				for i2 in range(4):
					if (i2 == i1):
						continue
					for i3 in range(4):
						if (i3 == i2 or i3 == i1):
							continue
						for i4 in range(4):
							if (i4 == i3 or i4 == i2 or i4 == i1):
								continue
							a = board[0][i1] + board[1][i2] + board[2][i3] + board[3][i4]
							mini = min(a, mini)  
		elif n == 3:
			for i1 in range(3):
				for i2 in range(3):
					if (i2 == i1):
						continue
					for i3 in range(3):
						if (i3 == i2 or i3 == i1):
							continue
						a = board[0][i1] + board[1][i2] + board[2][i3]
						mini = min(a, mini)	
		elif n == 2:
			mini = (min(board[0][0] + board[1][1], board[0][1] + board[1][0]))
		elif n== 1:
			mini = board[0][0]
		print(mini)

			

main()