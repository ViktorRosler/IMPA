import sys, math


def main():
	# sys.stdin = open('11505.txt', 'r')
	inp = sys.stdin.readlines()

	index = 1
	while index < len(inp):
		moves = int(inp[index].rstrip())
		index += 1

		x = 0 
		y = 0
		deg = 0		
		rad = 0
		for i in range(moves):
			a = inp[index].rstrip().split()
			index += 1

			val = int(a[1])

			if a[0][0] == 'f':
				x += math.cos(rad) * val
				y += math.sin(rad) * val

			elif a[0][0] == 'b':
				x -= math.cos(rad) * val
				y -= math.sin(rad) * val

			elif a[0][0] == 'l':
				deg += val
				rad = deg * math.pi / 180

			elif a[0][0] == 'r':
				deg -= val
				rad = deg * math.pi / 180

			#print(x,y, rad)

		print(round(math.dist((0,0), (x,y))))

		# rad = deg * math.pi / 180

main()