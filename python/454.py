import sys, math

def main():
	#sys.stdin = open('454.txt', 'r')
	inp = sys.stdin.readlines()
	index = 0
	cnt = int(inp[index].rstrip())
	index = 2
	while cnt > 0:
		words = []
		while True:
			init = inp[index].rstrip()
			index += 1
			words.append(init)
			if init == '' or index == len(inp):
				break
			
		words = sorted(words)
		for i in range(len(words)):
			for j in range(i+1, len(words)):
				if sorted(list(words[i].strip().replace(' ', ''))) == sorted(list(words[j].strip().replace(' ', ''))):
					print("{} = {}".format(words[i], words[j]))

		cnt -= 1
		if cnt > 0:
			print()
			


main()