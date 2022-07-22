import sys, math

def main():
	# sys.stdin = open('11100.txt', 'r')
	inp = sys.stdin.readlines()
	first_loop = True

	index = 0
	while True:
		bags_nr = int(inp[index].rstrip())
		index += 1

		if bags_nr == 0:
			break

		bags = []
		while len(bags) < bags_nr:
			bags += inp[index].rstrip().split(' ')
			index += 1

		for i in range(len(bags)):
			bags[i] = int(bags[i])
		bags.sort()
		for i in range(len(bags)):
			bags[i] = str(bags[i])
	
		rows = 1
		count = 1
		for i in range(1, bags_nr):
			if bags[i] == bags[i-1]:
				count += 1
			else:
				count = 1

			if count > rows:
				rows = count

		output = []
		for i in range(rows):
			output.insert(0, [])

		index2 = 0
		while index2 < bags_nr:
			for j in range(rows):
				output[j].append(bags[index2])
				index2 += 1
				if index2 == bags_nr:
					break

		if not first_loop:
			print('\n{:}'.format(len(output)))
		else:
			print(len(output))
			first_loop = False

		for i in output:
			print(' '.join(i))

main()
