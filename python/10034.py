""" solution based on Prim's algorithm:
    1. add any node to graph
    2. find the closest node to graph and add it, update total distance
    3. repeat step 2   """


import sys, math

def find_dist(node1, node2):
	return math.sqrt((node1[0]-node2[0])**2+(node1[1]-node2[1])**2)

def main():
	sys.stdin = open('10034.txt', 'r')
	inp = sys.stdin.readlines()

	index = 2
	first_loop = True
	while index < len(inp):
		freckles = int(inp[index].rstrip())
		index += 1
		dist = 0.0

		nodes_todo = []
		nodes_done = []	
		for i in range(freckles):
			node = inp[index].rstrip().split(' ')
			nodes_todo.append((float(node[0]), float(node[1])))
			index += 1

		nodes_done.append(nodes_todo.pop())
		while nodes_todo != []:
			min_dist = find_dist(nodes_done[0], nodes_todo[0])
			min_index = 0
			for i in range(len(nodes_done)):
				for j in range(len(nodes_todo)):
					d = find_dist(nodes_done[i], nodes_todo[j])
					if d < min_dist:
						min_dist = d
						min_index = j

			dist += min_dist
			nodes_done.append(nodes_todo.pop(min_index))
		index += 1
		if first_loop:
			print('{:4.2f}'.format(dist))
			first_loop = False
		else:
			print('\n{:4.2f}'.format(dist))

	
	
main()