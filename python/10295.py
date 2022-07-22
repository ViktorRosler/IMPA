import sys, math

def main():
	# sys.stdin = open('10295.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		init = inp[index].rstrip().split()
		index += 1

		words = int(init[0])

		hay_dict = {}
		for i in range(words):
			init = inp[index].rstrip().split()
			hay_dict[init[0]] = int(init[1])
			index += 1


		hay_points = 0
		while True:
			line = inp[index].rstrip().split()
			index += 1

			for i in hay_dict:	
				if i in line:
					hay_points += hay_dict[i] * line.count(i)

			if '.' in line:
				print(hay_points)
				if index >= len(inp):
					return
				else:
					hay_points = 0
					continue

main()