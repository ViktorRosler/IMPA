import sys, math

def main():
	sys.stdin = open('11753.txt', 'r')

	cases = int(sys.stdin.readline())

	for i in range(cases):
		inp = sys.stdin.readline().split()

		length = int(inp[0])
		diff = int(inp[1])

		arr = sys.stdin.readline().split()
		for n in arr:
			n = int(n)

		inserts = 0
		f_i = 0
		b_i = len(arr) - 1

		while (f_i + 1 < b_i):
			if arr[f_i] == arr[b_i]:
				f_i += 1
				b_i -= 1
			else:


main()