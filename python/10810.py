import sys, math

def main():
	sys.stdin = open('10810.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		init = int(inp[index].rstrip())
		index += 1

		if init == 0:
			break

		seq = []
		for i in range(init):
			seq.append(int(inp[index].rstrip()))
			index += 1

		count = 0
		for i in range(init):
			mini = math.inf
			for j in range(len(seq)):
				if seq[j] < mini:
					mini = seq[j]
					mini_index = j
			count += mini_index
			seq.pop(mini_index)
			
		

		print(count)


main()