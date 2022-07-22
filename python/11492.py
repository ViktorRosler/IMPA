import sys

sys.stdin = open("11492.txt")

while True:
	M = int(sys.stdin.readline())

	print(M)

	if M == 0:
		break

	a = sys.stdin.readline().strip().split()
	start = a[0]
	end = a[1]

	# print(start, end)

	dic1 = {}
	dic2 = {}
	dic3 = {}
	for i in range(M):
		b = sys.stdin.readline().strip().split()

		if b[0] not in dic1:
			dic1[b[0]] = []

		if b[1] not in dic1:
			dic1[b[1]] = [] 

		if b[2] not in dic2:
			dic2[b[2]] = [] 

		dic1[b[0]].append(b[2])
		dic1[b[1]].append(b[2])
		dic2[b[2]].append(b[0])
		dic2[b[2]].append(b[1])

	mini = 999999
	stack = []
	if start in dic1:
		for i in dic1[start]:
			for j in dic2[i]:
				if j != start:
					# print([len(i), [i], j])
					stack.append([len(i), [i], j])

		while len(stack) > 0:
			c = stack[-1]
			del stack[-1]

			if c[2] == end:
				mini = min(mini, c[0])
				continue

			if c[0] >= mini or c[0] > 40:
				continue

			if c[1][-1] not in dic3:
				dic3[c[1][-1]] = c[0]
			elif c[0] >= dic3[c[1][-1]]:
				continue
			else:
				dic3[c[1][-1]] = c[0]

			# print(c)

			for i in dic1[c[2]]:
				if i[0] != c[1][-1][0]:
					if i not in c[1]:
						if dic2[i][0] == dic2[i][1] or dic2[i][0] != c[2]:
							stack.append([c[0] + len(i),c[1] + [i], dic2[i][0]])
						else:
							stack.append([c[0] + len(i),c[1] + [i], dic2[i][1]])

						
	if mini == 999999:
		print("impossivel")
	else:
		print(mini)

