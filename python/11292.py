import sys, math

def main():
	#sys.stdin = open('11292.txt', 'r')

	while True:
		init = sys.stdin.readline().split()

		if init == ["0","0"]:
			break

		heads = int(init[0])
		knights = int(init[1])

		h = []
		k = []
		for i in range(heads):
			h.append(int(sys.stdin.readline()))

		for i in range(knights):
			k.append(int(sys.stdin.readline()))

		h.sort()
		k.sort()

		coin = 0
		index = 0
		win = True
		for i in h:
			while index < knights and k[index] < i:
				index += 1
			if index >= knights:
				win = False
				break
			coin += k[index]	
			index += 1
			

		if win:
			print(coin)
		else:
			print("Loowater is doomed!")


main()