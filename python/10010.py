import sys

def in_grid(rows, cols, x, y):
	return x >= 0 and x < rows and y >= 0 and y < cols

sys.stdin = open("10010.txt")

cases = int(sys.stdin.readline())

for i in range(cases):
	if i > 0:
		print()
	sys.stdin.readline()

	a = sys.stdin.readline().split()
	rows = int(a[0])
	cols = int(a[1])

	b = []
	for j in range(rows):
		b.append(sys.stdin.readline().strip())

	words = int(sys.stdin.readline())
	
	for j in range(words):
		word = sys.stdin.readline().strip()
		done = False
		for row in range(rows):
			for letter in range(cols):
				if b[row][letter].lower() == word[0].lower():
					# W
					x, y = row, letter
					for k in range(1, len(word)):
						y -= 1
						if not (in_grid(rows, cols, x, y) and b[x][y].lower() == word[k].lower()):
							break
					else:
						print(row+1, letter+1)
						done = True
						break

					# NW
					x, y = row, letter
					for k in range(1, len(word)):
						x -= 1
						y -= 1
						if not (in_grid(rows, cols, x, y) and b[x][y].lower() == word[k].lower()):
							break
					else:
						print(row+1, letter+1)
						done = True
						break

					# N
					x, y = row, letter
					for k in range(1, len(word)):
						x -= 1
						if not (in_grid(rows, cols, x, y) and b[x][y].lower() == word[k].lower()):
							break
					else:
						print(row+1, letter+1)
						done = True
						break

					# NE
					x, y = row, letter
					for k in range(1, len(word)):
						x -= 1
						y += 1
						if not (in_grid(rows, cols, x, y) and b[x][y].lower() == word[k].lower()):
							break
					else:
						print(row+1, letter+1)
						done = True
						break

					# E
					x, y = row, letter
					for k in range(1, len(word)):
						y += 1
						if not (in_grid(rows, cols, x, y) and b[x][y].lower() == word[k].lower()):
							break
					else:
						print(row+1, letter+1)
						done = True
						break

					# SE
					x, y = row, letter
					for k in range(1, len(word)):
						x += 1
						y += 1
						if not (in_grid(rows, cols, x, y) and b[x][y].lower() == word[k].lower()):
							break
					else:
						print(row+1, letter+1)
						done = True
						break

					# S
					x, y = row, letter
					for k in range(1, len(word)):
						x += 1
						if not (in_grid(rows, cols, x, y) and b[x][y].lower() == word[k].lower()):
							break
					else:
						print(row+1, letter+1)
						done = True
						break

					# SW
					x, y = row, letter
					for k in range(1, len(word)):
						x += 1
						y -= 1
						if not (in_grid(rows, cols, x, y) and b[x][y].lower() == word[k].lower()):
							break
					else:
						print(row+1, letter+1)
						done = True
						break

				if done:
					break
			if done:
				break


