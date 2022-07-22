import sys, math
from collections import deque

def main():
	sys.stdin = open('663.txt', 'r')

	while True:
		size = 2 * int(sys.stdin.readline())

		if size == 0:
			break

		inp = sys.stdin.readline().split()
		start = (int(inp[0]),int(inp[1])) 

		inp = sys.stdin.readline().split()
		end = (int(inp[0]),int(inp[1])) 

		step = -1
		done = set()
		while True:
			inp = sys.stdin.readline().split()
			if inp[0] == "0":
				break
			done.add((int(inp[0]),int(inp[1])))

		todo = set()
		todo.add(start)
		nxt = set()
		finished = False
		while len(todo) > 0:
			step += 1
			for i in todo:
				

				#print(i ,end)

				if i == end:
					if i not in done:
						print("Result :", step)
						finished = True
					todo = set()
					break



				done.add(i)

				
				if i[0] + 2 <= size:
					# diagonal
					if i[1] + 2 <= size:
						if (i[0]+2, i[1]+2) not in done:
							nxt.add((i[0]+2, i[1]+2))
					# knight
					if i[1] + 1 <= size:
						if (i[0]+2, i[1]+1) not in done:
							nxt.add((i[0]+2, i[1]+1))
					# knight
					if i[1] - 1 >= 0:
						if (i[0]+2, i[1]-1) not in done:
							nxt.add((i[0]+2, i[1]-1))
					# diagonal
					if i[1] - 2 >= 0:
						if (i[0]+2, i[1]-2) not in done:
							nxt.add((i[0]+2, i[1]-2))
				if i[0] - 2 >= 0:
					# diagonal
					if i[1] + 2 <= size:
						if (i[0]-2, i[1]+2) not in done:
							nxt.add((i[0]-2, i[1]+2))
					# knight
					if i[1] + 1 <= size:
						if (i[0]-2, i[1]+1) not in done:
							nxt.add((i[0]-2, i[1]+1))
					# knight
					if i[1] - 1 >= 0:
						if (i[0]-2, i[1]-1) not in done:
							nxt.add((i[0]-2, i[1]-1))
					# diagonal
					if i[1] - 2 >= 0:
						if (i[0]-2, i[1]-2) not in done:
							nxt.add((i[0]-2, i[1]-2))	
				if i[0] + 1 <= size:
					# knight
					if i[1] + 2 <= size:
						if (i[0]+1, i[1]+2) not in done:
							nxt.add((i[0]+1, i[1]+2))
					# knight
					if i[1] - 2 >= 0:
						if (i[0]+1, i[1]-2) not in done:
							nxt.add((i[0]+1, i[1]-2))
				if i[0] - 1 >= 0:
					# knight
					if i[1] + 2 <= size:
						if (i[0]-1, i[1]+2) not in done:
							nxt.add((i[0]-1, i[1]+2))
					# knight
					if i[1] - 2 >= 0:
						if (i[0]-1, i[1]-2) not in done:
							nxt.add((i[0]-1, i[1]-2))

				# tele
				if (size - i[0] + 1, i[1]) not in done:
					nxt.add((size - i[0] + 1, i[1]))
				if (i[0], size - i[1] + 1) not in done:
					nxt.add((i[0], size - i[1] + 1))

			todo = nxt
			nxt = set()
			

		if not finished:
			print("Solution doesn't exist")
			

main()