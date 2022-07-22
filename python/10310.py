import sys, math

def main():
	# sys.stdin = open('10310.txt', 'r')
	index = 0
	inp = sys.stdin.readlines()

	while index < len(inp):
		init = inp[index].rstrip().split(' ')
		index += 1

		can_escape = False
		nr_holes = int(init[0])
		gopher = (float(init[1]), float(init[2]))
		dog = (float(init[3]), float(init[4]))
	
		for i in range(nr_holes):
			hole = inp[index].rstrip().split(' ')
			hole_x = float(hole[0])
			hole_y = float(hole[1])
			index += 1

			gopher_dist = math.sqrt((gopher[0] - hole_x)**2 + (gopher[1] - hole_y)**2)
			dog_dist = math.sqrt((dog[0] - hole_x)**2 + (dog[1] - hole_y)**2)

			if not can_escape and gopher_dist * 2 <= dog_dist:
				esc_hole = (hole_x, hole_y)
				can_escape = True

		index += 1

		if can_escape:
			print('The gopher can escape through the hole at ({:5.3f},{:5.3f}).'.format(esc_hole[0], esc_hole[1]))
		else:
			print('The gopher cannot escape.')


main()