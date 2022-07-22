

import sys, math


def main():
	#sys.stdin = open('11855.txt')
	while True:
		inp = sys.stdin.readline().strip()
		inp = "".join(inp.split())
		if inp == "":
			return;
		res = [inp[i: j] for i in range(len(inp)) for j in range(i + 1, len(inp) + 1)] 
		#print(res)
		
		not_done = True;
		length = 1
		while not_done:
			dic = {}
			for i in range(len(inp)-length + 1):
				s = inp[i:i+length]
				if s not in dic:
					dic[s] = 1
				else:
					dic[s] += 1
			a = sorted(dic.values(), reverse=True)
			if a[0] > 1:
				print(a[0])
				length += 1
			else:
				not_done = False
		print()



main()