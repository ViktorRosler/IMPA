import sys, math



def main():
	sys.stdin = open('10917.txt', 'r')

	while True:
		init = sys.stdin.readline().split()

		if init[0] == '0':
			return

		inter = int(init[0])
		paths = int(init[1])

		dp = {}
		dp2 = {}
		for i in range(paths):
			init = sys.stdin.readline().split()
			if init[0] not in dp:
				dp[init[0]] = []
				dp2[init[0]] = []
			if init[1] not in dp:
				dp[init[1]] = []
				dp2[init[1]] = []
			dp[init[0]].append((init[1], int(init[2])))
			dp[init[1]].append((init[0], int(init[2])))
			dp2[init[0]].append(init[1])
			dp2[init[1]].append(init[0])



		
		nodes = {}
		nodes['2'] = 0
		go_on = True
		#print(dp)
		while go_on:
			go_on = False
			cost = math.inf
			node = ''
			for i in nodes:
				if i not in dp or len(dp[i]) == 0:
					continue
				go_on = True
				n = dp[i].pop(-1)
				if n[0] not in nodes or n[1] <= nodes[n[0]]:
					node = i
					cost = n[1]		
					break
			if cost != math.inf:
				if n[0] not in nodes:
					nodes[n[0]] = cost + nodes[node]
				else:
					nodes[n[0]] = min(nodes[n[0]], cost + nodes[node])
				

		s = 0

	
		nodes2 = sorted(list(nodes.items()), key=lambda x:x[1], reverse=True)
		done = {'1':1, '2':0}
		#print(dp2, nodes, nodes2)
		for i in nodes2:			
			if i[0] not in nodes or nodes['1'] < i[1]:
				continue
			if i[0] not in dp2 or i[0] not in done:
				continue
			for j in dp2[i[0]]:
				if i[1] <= nodes[j]:
					continue
				if j not in done:
					done[j] = done[i[0]]
				else:
					done[j] += done[i[0]]
			#print(done)

		print(inter, paths, nodes2)
		print(done['2'])
		


					

main()