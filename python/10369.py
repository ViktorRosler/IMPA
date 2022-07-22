import sys, math

def find_dist(node1, node2):
	return math.hypot(node1[0]-node2[0], node1[1]-node2[1])

def main():
	# sys.stdin = open('10369.txt', 'r')
	inp = sys.stdin.readlines()

	index = 1
	while index < len(inp):
		init = inp[index].rstrip().split(' ')
		index += 1

		sat = int(init[0])
		posts_nr = int(init[1])

		nodes = []
		for i in range(posts_nr):
			init = inp[index].rstrip().split(' ')
			index += 1
			if i == 0:
				nodes.append([int(init[0]), int(init[1]), 0])
			else:
				nodes.append([int(init[0]), int(init[1]), math.inf])


		for i in range(len(nodes)):
			# print(nodes)
			min_dist = math.inf
			for j in range(i+1, len(nodes)):
				dist = find_dist(nodes[i], nodes[j])
				if dist < nodes[j][2]:
					nodes[j][2] = dist
				if nodes[j][2] < min_dist:
					min_dist = nodes[j][2]
					k = j
			if i < len(nodes)-1:
				temp = nodes[i+1]
				nodes[i+1] = nodes[k]
				nodes[k] = temp

		edges=[]
		for i in nodes:
			edges.append(i[2])

		'''print(nodes)
		print(edges)'''

		for i in range(sat-1):
			edges.remove(max(edges))

		print('{:.2f}'.format(max(edges)))

main()