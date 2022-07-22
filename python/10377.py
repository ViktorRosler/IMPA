import sys, math




def main():
	sys.stdin = open('10377.txt', 'r')

	cases = int(sys.stdin.readline())
	sys.stdin.readline()

	for c in range(cases):
		init = sys.stdin.readline().split()
		rows = int(init[0])
		cols = int(init[1])

		mapp = [[0 for i in range(cols)] for j in range(rows)]
		for i in range(rows):
			line = sys.stdin.readline()
			for j in range(cols):
				if line[j] == "*":
					mapp[i][j] = 1


		dire = "N"
		inp = sys.stdin.readline().split()
		row = int(inp[0]) - 1
		col = int(inp[1]) - 1

		if (c>0):
			print()

		done = False
		while(True):
			if done:
				break

			inp = sys.stdin.readline()

			for char in inp:
				if char == "R":
					if dire == "N":
						dire = "E"
					elif dire == "E":
						dire = "S"
					elif dire == "S":
						dire = "W"
					elif dire == "W":
						dire = "N"		
				elif char == "L":
					if dire == "N":
						dire = "W"
					elif dire == "E":
						dire = "N"
					elif dire == "S":
						dire = "E"
					elif dire == "W":
						dire = "S"
				elif char == "F":
					if dire == "N" and row > 0:
						if mapp[row-1][col] != 1:
							row -= 1
					elif dire == "E" and col < cols-1:
						if mapp[row][col+1] != 1:
							col += 1
					elif dire == "S" and row < rows-1:
						if mapp[row+1][col] != 1:
							row += 1
					elif dire == "W" and col > 0:
						if mapp[row][col-1] != 1:
							col -= 1	
				elif char == "Q":
					sys.stdin.readline()
					print(row+1,col+1,dire)
					done = True
					break

main()