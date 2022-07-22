import sys, math, re

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


		sub_len = 9999
		out = []
		done = False
		while sub_len > 0:
			dp1 = {}
			for i in short_words:
				if sub_len == 9999:
					sub_len = max_size

				dp2 = set()

	
				for j in range(len(i)+1-sub_len):
					sub_word = i[j:sub_len+j]

					if sub_word in dp2:
						continue
					else:
						if sub_word in dp1:
							dp1[sub_word] += 1
						else:
							dp1[sub_word] = 1
					dp2.add(sub_word)

			for i in dp1:
				for j in long_words:
					if i in j:
						dp1[i] += 1
				if dp1[i] * 2 > init:
					out.append(i)
					done = True
					
			if done:
				break

			sub_len -= 1
			
		
		if len(out) == 0:
			print('?')
		else:
			for i in sorted(out):
				print(i)

		
		if index+1 < len(inp):
			print()

main()