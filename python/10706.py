import sys, math

def main():
	sys.stdin = open('10706.txt', 'r')

	cases = int(sys.stdin.readline())

	for i in range(cases):

		inp = int(sys.stdin.readline())

		a = 1
		b = 1
		while (b < inp):
			inp -= b
			if a < 9:
				b += 1
			elif a < 99:
				b += 2
			elif a < 999:
				b += 3
			elif a < 9999:
				b += 4
			elif a < 99999:
				b += 5
			a += 1

		#print(inp)

		s = ""
		j = 1
		while (len(s)-1 < inp):
			s += str(j)
			j += 1

		print(s[inp-1])



main()