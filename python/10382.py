import sys, math

def main():
	#sys.stdin = open('10382.txt', 'r')

	ind = 0
	while True:
		ind += 1
		init = sys.stdin.readline().split()

		if len(init) < 1:
			break

		nr_sprinks = int(init[0])
		length = int(init[1])
		width = int(init[2])

		sprinklers = []
		for i in range(nr_sprinks):
			inp = sys.stdin.readline().split()

			a = int(inp[0])
			b = int(inp[1])

			if b*2 < width:
				continue

			c = math.sqrt(b**2 - (width/2)**2)

			
			sprinklers.append((a-c,a+c))
	


		sprinklers.sort()
		total = 0
		dist = 0
		index = 0
		#if ind == 98:
			#print(sprinklers, length)
		while index < len(sprinklers) and dist < length:
			if dist < sprinklers[index][0]:
				total = -1
				break

			new_dist = dist
			while  index < len(sprinklers) and dist >= sprinklers[index][0]:
				new_dist = max(new_dist, sprinklers[index][1])
				index += 1

			total += 1
			dist = new_dist

		if total == 0 or dist < length:
			total = -1
		print(total)
main()