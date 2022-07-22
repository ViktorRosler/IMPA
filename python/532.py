import sys, math


def main():
	# sys.stdin = open('532.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		init = inp[index].rstrip().split()
		index += 1

		L = int(init[0])
		R = int(init[1])
		C = int(init[2])

		if L == R == C == 0:
			return

		# (Level, Row, Col)
		mapp = {}
		for i in range(L):
			for j in range(R):
				init = inp[index].rstrip()
				index += 1
				for k in range(C):
					if init[k] == 'S':
						start = (i,j,k)
						mapp[(i,j,k)] = 0
					elif init[k] == 'E':
						end = (i,j,k)
						mapp[(i,j,k)] = -1
					elif init[k] == '.':
						mapp[(i,j,k)] = -1		
			index += 1

		next_tile = [start]
		path = 1
		while len(next_tile) > 0:
			tmp = []
			for i in next_tile:
	
				tile = (i[0]+1, i[1], i[2])
				if tile in mapp:
					if mapp[tile] == -1:
						mapp[tile] = path
						tmp.append(tile)

				tile = (i[0]-1, i[1], i[2])
				if tile in mapp:
					if mapp[tile] == -1:
						mapp[tile] = path
						tmp.append(tile)


				tile = (i[0], i[1]+1, i[2])
				if tile in mapp:
					if mapp[tile] == -1:
						mapp[tile] = path
						tmp.append(tile)

				tile = (i[0], i[1]-1, i[2])
				if tile in mapp:
					if mapp[tile] == -1:
						mapp[tile] = path
						tmp.append(tile)
	
				tile = (i[0], i[1], i[2]+1)
				if tile in mapp:
					if mapp[tile] == -1:
						mapp[tile] = path
						tmp.append(tile)

				tile = (i[0], i[1], i[2]-1)
				if tile in mapp:
					if mapp[tile] == -1:
						mapp[tile] = path
						tmp.append(tile)
			path += 1
			next_tile = tmp
		
		time = mapp[end]
		if time == -1:
			print('Trapped!')
		else:
			print(f'Escaped in {time} minute(s).')

main()