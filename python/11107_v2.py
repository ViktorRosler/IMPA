import sys, math

def main():
	sys.stdin = open('11107.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		init = int(inp[index].rstrip())
		index += 1

		if init == 0:
			return

		half = math.ceil(init / 2)

		long_words = []
		short_words = []
		lengths  = []
		for i in range(init):
			long_words.append(inp[index].rstrip())
			index += 1
			lengths.append(len(long_words[i]))

				
		while len(lengths) > 0 and len(short_words) < half:
			i = lengths.index(min(lengths))
			short_words.append(long_words[i])
			max_size = lengths[i]
			del lengths[i]
			del long_words[i]

main()