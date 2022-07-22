import sys, math

def main():
	sys.stdin = open('939.txt', 'r')

	lines = int(sys.stdin.readline())

	dic = {}
	TODO = {}
	for i in range(lines):
		init = sys.stdin.readline().split()

		if init[1] == "non-existent" or init[1] == "recessive" or init[1] == "dominant":
			dic[init[0]] = init[1]
		else:
			if init[1] in TODO:
				TODO[init[1]].append(init[0])
			else:
				TODO[init[1]] = [init[0]]

	done = False
	while not done:
		done = True
		for key,value in TODO.items():
			if key not in dic and len(value) == 2:
				if value[0] in dic and value[1] in dic:
					a = dic[value[0]]
					b = dic[value[1]]

					if a == "dominant" and b == "dominant":
						c = "dominant"
					elif a == "dominant" and b == "recessive":
						c = "dominant"
					elif a == "recessive" and b == "dominant":
						c = "dominant"
					elif a == "dominant" or b == "dominant":
						c = "recessive"
					elif a == "recessive" and b == "recessive":
						c = "recessive"
					else:
						c = "non-existent"

					dic[key] = c
					done = False

	a = sorted(dic.items())
	for i in a:
		print(i[0], i[1])


main()	