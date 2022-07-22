import sys, math

def main():
	#sys.stdin = open('11561.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		init = inp[index].rstrip().split()
		index += 1
		col = int(init[0])
		row = int(init[1])
		mapp = {}
		todo = []
		for i in range(row):
			a = inp[index].rstrip()
			index += 1
			for j in range(col):
				mapp[(i,j)] = a[j]
				if a[j] == 'P':
					todo.append((i,j))
		cnt = 0
		done = set()			
		while todo:
			a = todo.pop()
			if a in done:
				continue
			done.add(a)
			if mapp[a] == 'G':
				cnt += 1
			N = (a[0]-1, a[1])
			E = (a[0], a[1]+1)
			S = (a[0]+1, a[1])
			W = (a[0], a[1]-1)
			if mapp[N] == 'T' or mapp[E] == 'T' or mapp[S] == 'T' or mapp[W] == 'T':
				continue
			if mapp[N] == '.' or mapp[N] == 'G':
				todo.append(N)
			if mapp[E] == '.' or mapp[E] == 'G':
				todo.append(E)
			if mapp[S] == '.' or mapp[S] == 'G':
				todo.append(S)
			if mapp[W] == '.' or mapp[W] == 'G':
				todo.append(W)

		print(cnt)

main()