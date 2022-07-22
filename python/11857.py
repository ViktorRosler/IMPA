import sys, math, heapq

def prims(graph):
    highest = -1                  
    explored = set()            
    start = next(iter(graph))   
    unexplored = [(0, start)]   
    while unexplored:
        cost, winner = heapq.heappop(unexplored)
        if winner not in explored:
            explored.add(winner)
            highest = max(highest, cost)
            for neighbour in graph[winner]:
                if neighbour not in explored:
                    heapq.heappush(unexplored, (graph[winner][neighbour], neighbour))
    return (highest, explored)

def main():
	#sys.stdin = open('11857.txt', 'r')

	while True:
		init = sys.stdin.readline().split()
		city_nr = int(init[0])
		road_nr = int(init[1])
		if city_nr == road_nr == 0:
			return
		if city_nr > road_nr + 2:
			for i in range(road_nr):
				 sys.stdin.readline()
			print('IMPOSSIBLE')
			continue

		w = {}	
		for i in range(road_nr):
			b = sys.stdin.readline().split()

			if b[0] not in w:
				w[b[0]] = {}
			if b[1] not in w:
				w[b[1]] = {}
			if b[1] not in w[b[0]]:
				w[b[0]][b[1]] = int(b[2])
				w[b[1]][b[0]] = int(b[2])
			elif w[b[0]][b[1]] > int(b[2]):
				w[b[0]][b[1]] = int(b[2])
				w[b[1]][b[0]] = int(b[2])
	
		if len(w) > 0:
			result = prims(w)
		else:
			print('IMPOSSIBLE')
			continue

		if len(result[1]) < city_nr:
			print('IMPOSSIBLE')
		else:
			print(result[0])

main()