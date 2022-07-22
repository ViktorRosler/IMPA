import sys, math

def main():
	#sys.stdin = open('10227.txt', 'r')

	
	init = sys.stdin.readline()
	trash = sys.stdin.readline()

	for i in range(int(init)):
		inp = sys.stdin.readline().split()

		ppl = int(inp[0])
		trees = int(inp[1])

		dic = {}
		for j in range(1,ppl+1):
			dic[str(j)] = ["0"]

		inp = sys.stdin.readline()
		while len(inp) > 1:
			inp = inp.split()

			if inp[1] not in dic[inp[0]]:
				dic[inp[0]].append(inp[1])

			inp = sys.stdin.readline()
		
		st = set()
		for value in dic.values():
			st.add(''.join([elem for elem in sorted(value)]))

		if i > 0:
			print()
		print(len(st))

main()