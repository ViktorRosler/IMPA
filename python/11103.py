import sys, math

def main():
	# sys.stdin = open('11103.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		init = inp[index].rstrip()
		index += 1

		if init == '0':
			return

		
		pqrst = []
		KACE = []
		N = []
		for s in init:
			if s == 'N':
				N.append(s)
			elif s == 'K' or s == 'A' or s == 'C' or s == 'E':
				KACE.append(s)
			elif s == 'p' or s == 'q' or s == 'r' or s == 's' or s == 't':
				pqrst.append(s)


		out = ''
		while len(pqrst) > 0:
			if out == '':
				out = pqrst.pop()
				while len(N)>0:
					out = N.pop() + out
				continue

			if len(KACE) > 0:
				out = KACE.pop() + pqrst.pop() + out
			else:
				break

		if out:
			print(out)
		else:
			print('no WFF possible')

main()