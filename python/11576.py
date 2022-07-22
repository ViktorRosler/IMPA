import sys, math

def main():
	#sys.stdin = open('11576.txt', 'r')
	inp = sys.stdin.readlines()

	index = 1
	while index < len(inp):
		init = inp[index].rstrip().split()
		index += 1

		k = int(init[0])
		w = int(init[1])

		l = k
		a = inp[index].rstrip()
		index += 1
		for i in range(1, w):
			b = inp[index].rstrip()
			index += 1
			for j in range(k):
				if a[j:] == b[:k-j]:
					l += j
					break
			else:
				l += k
			a = b
		print(l)



main()