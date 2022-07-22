import sys, math

def main():
	sys.stdin = open('11503.txt', 'r')

	cases = int(sys.stdin.readline())

	
	for i in range(cases):
		F = int(sys.stdin.readline())

		dic = {}
		for i in range(F):
			a = sys.stdin.readline().split()

			if a[0] not in dic:
				dic[a[0]] = set()
			
			if a[1] not in dic:
				dic[a[1]] = set()

			dic[a[0]].add(a[1])
			dic[a[1]].add(a[0])

			dic[a[0]] = dic[a[0]].union(dic[a[1]])

			dic[a[1]] = dic[a[0]]

			c = l[-1]
			for j in l[-1]:
				for k in l:
					if j in k:
						c = c.union(k)



			print(len(dic[a[0]].union(dic[a[1]])))




main()