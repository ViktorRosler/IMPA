import sys, math



def main():
	#sys.stdin = open('1757.txt')
	inp = sys.stdin.readlines()
	index = 0
	while index < len(inp):
		case = inp[index].split()
		index += 1

		trans = int(case[0])
		pair = int(case[1])

		dic = {}
		for i in range(trans):
			a = inp[index].split()
			index += 1

			if a[0] not in dic:
				dic[a[0]] = set()
			dic[a[0]].add(a[1])

		for i in range(pair):
			a = inp[index].split()
			index += 1

			word1 = a[0]
			word2 = a[1]

			if len(word1) != len(word2):
				print("no")
				continue

			for j in range(len(word1)):
				if word1[j] == word2[j]:
					continue
				if word1[j] not in dic:
					print("no")
					break

				todo = []
				done = set()
				for k in dic[word1[j]]:
					todo.append(k)

				found = False
				while todo:
					a = todo.pop()
					done.add(a)

					if a == word2[j]:
						found = True
						break

					if a in dic:
						for l in dic[a]:
							if l not in done:
								todo.append(l)

				if found:
					continue
				else:
					print("no")
					break
			else:
				print("yes")

main()