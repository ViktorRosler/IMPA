import sys, math

def main():
	# sys.stdin = open('11686.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		init = inp[index].rstrip().split()
		index += 1

		sticks = int(init[0])
		lines = int(init[1])

		dic = {}
		dic2 = {}

		for i in range(1, sticks+1):
			dic[str(i)] = []
			dic2[str(i)] = []

		for i in range(lines):
			line = inp[index].rstrip().split()
			index += 1

			dic[line[1]].append(line[0])
			dic2[line[0]].append(line[1])

		imp = False
		out = []
		while len(dic) > 0:
			a = dic.copy()
			brk = True
			for i in a:
				if dic[i] == []:
					out.append(i)
					del dic[i]
					for j in dic2[i]:
						dic[j].remove(i)
					brk = False

			if brk:
				imp = True
				break

		if imp:
			print('IMPOSSIBLE') 
		else:
			for i in out:
				print(i)




main()