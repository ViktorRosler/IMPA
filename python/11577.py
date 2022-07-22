import sys, math

def main():
	# sys.stdin = open('11577.txt', 'r')
	inp = sys.stdin.readlines()

	index = 1
	while index < len(inp):
		init = inp[index].strip()
		index += 1

		init = init.lower()
		maximum = 0
		out = []
		for i in range(26):
			cnt = init.count(chr(97+i))
			if cnt == maximum:
				out.append(chr(97+i))
				continue
			elif cnt > maximum:
				maximum = cnt
				out = [chr(97+i)]

		print(''.join(sorted(out)))


main()