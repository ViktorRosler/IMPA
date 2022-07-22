import sys, math

def main():
	sys.stdin = open('11987.txt', 'r')

	init = sys.stdin.readline().split()
	ints = int(init[0])
	commands = int(init[1])

	index = 0

	sets = {}
	for i in range(1, ints+1):
		sets[i] = set()
		sets[i].add(i)


	for i in range(commands):
		init = sys.stdin.readline().split()

		fst = int(init[0])
		snd = int(init[1])

		if fst == 1:
			trd = int(init[2])
			a = sets[snd].union(sets[trd])
			for j in a:
				sets[j] = a
		elif fst == 2:
			trd = int(init[2])
			for j in sets[trd].copy():
				sets[j].add(snd)
			for j in sets[snd].copy():
				if snd in sets[j]:
					sets[j].remove(snd)
			sets[snd] = sets[trd]
		else:
			summa = 0
			start = True
			for i in sets[snd]:
				summa += i
			print(len(sets[snd]), summa)



main()