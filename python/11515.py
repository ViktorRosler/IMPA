import sys, math

def is_valid(cranes, valid):
	for i in cranes:
		for j in cranes:
			if i != j:
				if i not in valid or j not in valid[i]:
					return False
	return True
def main():
	#sys.stdin = open('11515.txt', 'r')

	cases = int(sys.stdin.readline())

	index = 0
	while index < cases:
		index += 1
		locs = int(sys.stdin.readline())

		asdf = []

		for i in range(locs):
			crane = sys.stdin.readline().split()
			x = int(crane[0])
			y = int(crane[1])
			z = int(crane[2])
			asdf.append((x,y,z))

		valid = {}
		for i in asdf:
			for j in asdf:
				if i != j:
					if math.dist((i[0],i[1]),(j[0],j[1])) > i[2] + j[2]:
						if i not in valid:
							valid[i] = set()
						valid[i].add(j) 

		max_area = 0
		for i in range(1, 2**locs+1):
			cranes = []

			j = 1
			ind = 0
			while j < 2**locs:
				if i & j:
					cranes.append(asdf[ind])
				j = j << 1
				ind += 1

			if not is_valid(cranes, valid):
				continue

			area = 0
			for i in cranes:
				area += i[2]**2

			if area > max_area:
				max_area = area

		print(max_area)
			
				
main()