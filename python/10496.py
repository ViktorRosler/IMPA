import sys, math, copy

def calc(asdf):
	if len(asdf[0]) == beepers:
		if (asdf[0][-1],-1) not in dic:
			dic[(asdf[0][-1],-1)] = abs(x_pos - beeper_pos[asdf[0][-1]][0]) + abs (y_pos - beeper_pos[asdf[0][-1]][1])
			dic[(-1,asdf[0][-1])] = dic[(asdf[0][-1],-1)]

		a = asdf[1][0] + dic[(asdf[0][-1],-1)]
		global mini
		mini = min(mini, a)
		return

	
	for i in range(beepers):
		if i not in asdf[0]:	
			b = copy.deepcopy(asdf)
			if (asdf[0][-1],i) not in dic:
				dic[(asdf[0][-1],i)] = abs(beeper_pos[i][0] - beeper_pos[asdf[0][-1]][0]) + abs (beeper_pos[i][1] - beeper_pos[asdf[0][-1]][1])
				dic[(i,asdf[0][-1])] = dic[(asdf[0][-1],i)]

			b[1][0] += dic[(b[0][-1],i)]
			b[0].append(i)
			calc(b)


def main():
	sys.stdin = open('10496.txt', 'r')

	scen = int(sys.stdin.readline())

	for i in range(scen):
		init = sys.stdin.readline().split()

		x = int(init[0])
		y = int(init[1])

		init = sys.stdin.readline().split()

		global x_pos, y_pos
		x_pos = int(init[0])
		y_pos = int(init[1])

		global beepers
		beepers = int(sys.stdin.readline())

		global mini
		mini = math.inf

		global dic
		dic = {}

		global beeper_pos 
		beeper_pos = []

		for i in range(beepers):
			init = sys.stdin.readline().split()
			bx = int(init[0])
			by = int(init[1])
			beeper_pos.append((bx,by))
			

		for i in range(len(beeper_pos)):
			dic[(-1,i)] = abs(x_pos - beeper_pos[i][0]) + abs (y_pos - beeper_pos[i][1])
			dic[(i,-1)] = dic[(-1,i)]
			calc(([i],[dic[(-1,i)]]))

		print(mini)

main()