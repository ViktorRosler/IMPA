import sys, math

cnt = 0

def balance(tree, node):
	global cnt

	for i in tree[node][2]:
		balance(tree, i)

	if tree[node][1] == '':
		return

	while tree[node][0] != 1:
		if tree[node][0] < 1:
			tree[node][0] += 1
			tree[tree[node][1]][0] -= 1
		else:
			tree[node][0] -= 1
			tree[tree[node][1]][0] += 1
		cnt += 1




def main():
	#sys.stdin = open('10672.txt', 'r')
	global cnt

	while True:
		init = int(sys.stdin.readline())

		if init == 0:
			return

		cnt = 0
		tree = {}
		for i in range(init):
			a = sys.stdin.readline().split()
			if a[0] not in tree:
				tree[a[0]] = [int(a[1]), '', []]
			else:
				tree[a[0]][0] = int(a[1])
			for i in range(3, 3+int(a[2])):
				tree[a[0]][2].append(a[i])
				if a[i] not in tree:
					tree[a[i]] = [-1, a[0], []]
				else:
					tree[a[i]][1] = a[0]

		for i in tree.items():
			if i[1][1] == '':
				root = i[0]
				

		balance(tree, root)
		print(cnt)



main()