import sys, math
from collections import deque

def main():
	sys.stdin = open('429.txt', 'r')

	init = int(sys.stdin.readline().strip())
	sys.stdin.readline()

	while (init > 0):
		init -= 1

		words = []

		while (True):
			word = sys.stdin.readline().strip()
			if (word == "*"):
				break
			words.append(word)


		while (True):
			line = sys.stdin.readline().split()

			if (line == []):
				break

			s = line[0]
			t = line[1]

			q = []
			trans = {}

			trans[s] = 0
			q.append(s)

			while (len(q) > 0 and t not in trans):
				u = q[0]
				del q[0]

				for i in range(len(words)):
					v = words[i]

					if (v not in trans and len(u) == len(v)):
						diff = 0
						for j in range(len(u)):
							if (u[j] != v[j]):
								diff += 1
						if (diff == 1):
							trans[v] = trans[u] + 1
							q.append(v)


			print(s, t, trans[t])
		if (init > 0):
			print()
main()