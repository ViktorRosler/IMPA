import sys, math

def main():
	# sys.stdin = open('10201.txt', 'r')
	inp = sys.stdin.readlines()

	index = 2
	while index < len(inp):
		total_dist = int(inp[index].rstrip())
		index += 1


		all_stops = []
		while index < len(inp):
			line = inp[index]
			index += 1

			if line == '\n':
				break

			line = line.rstrip().split(' ')
			if int(line[0]) <= total_dist: 
				all_stops.append((int(line[0]), int(line[1])))

		all_stops.append((total_dist+100, 9999))

		dist = 0
		gas = 100
		total_cost = 0
		possible = False

		while dist + gas < total_dist + 100:
			inrange_stops = []
			for stop in all_stops:
				if dist < stop[0] <= dist+gas:
					inrange_stops.append(stop)

			if inrange_stops == []:
				break

			next_stop = inrange_stops[0]
			for stop in inrange_stops:
				if stop[1] < next_stop[1]:
					next_stop = stop

			gas -= (next_stop[0] - dist)
			dist = next_stop[0]
			current_cost = next_stop[1]

			inrange_stops = []
			for stop in all_stops:
				if dist < stop[0] <= dist+200 and stop[0] < total_dist:
					if stop[1] < current_cost:
						dist_left = stop[0] - dist
						if dist_left > gas:
							total_cost += (dist_left - gas) * current_cost
							gas = dist_left
						break
			else:
				dist_left = (total_dist + 100) - dist
				if dist_left < 200:
					total_cost += (dist_left-gas) * current_cost
					gas = dist_left
				else:
					total_cost += (200-gas) * current_cost
					gas = 200
		else:
			possible = True

		if possible:
			print(total_cost)
		else:
			print('Impossible')

		if index < len(inp):
			print()

main()