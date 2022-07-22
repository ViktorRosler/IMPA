import sys, math

def main():
	#sys.stdin = open('10370.txt', 'r')

	init = sys.stdin.readline()


	for i in range(int(init)):
		inp = sys.stdin.readline().split()
		ppl = int(inp[0])

		total = 0.0
		for j in range(1, len(inp)):
			total += int(inp[j])
		avg = total / ppl

		abv = 0.0
		for j in range(1,len(inp)):
			if int(inp[j]) > avg:
				abv += 1

		print("{:.3f}%".format(100*abv/ppl))

main()