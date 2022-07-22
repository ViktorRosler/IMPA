import sys, math

def main():
	sys.stdin = open('11572.txt', 'r')

	cases = int(sys.stdin.readline()) 

	for i in range(cases):
		flakes = int(sys.stdin.readline())

		back = 0
		m = 0
		r = 0
		s = set()
		d = {}
		for i in range(1,flakes+1):
			n = int(sys.stdin.readline())
			if n in s:
				back = max(back,d[n])
			else:
				s.add(n)
			d[n] = i
			#print(back,d)
			m = max(i-back,m)

		print(m)

main()