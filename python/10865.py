import sys, math

def main():
	# sys.stdin = open('10865.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		init = int(inp[index].rstrip())
		index += 1

		if init == 0:
			return

		coords = []
		for i in range(init):
			coord = inp[index].rstrip().split(' ')
			coords.append((coord[0],coord[1]))
			index += 1

		mid = coords.pop(init // 2)

		Stan = 0
		Ollie = 0
		for i in coords:
			if int(i[0]) > int(mid[0]) and int(i[1]) > int(mid[1]):
				Stan += 1
			elif int(i[0]) < int(mid[0]) and int(i[1]) < int(mid[1]):
				Stan += 1
			elif int(i[0]) < int(mid[0]) and int(i[1]) > int(mid[1]):
				Ollie += 1
			elif int(i[0]) > int(mid[0]) and int(i[1]) < int(mid[1]):
				Ollie += 1

		print(str(Stan) + ' ' + str(Ollie))

main()