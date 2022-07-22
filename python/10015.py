import sys, math

def main():
	# sys.stdin = open('10015.txt', 'r')
	inp = sys.stdin.readlines()

	primes = []
	for i in range(2,100000):
		for j in range(2, int(math.sqrt(i))+1):
			if i % j == 0:
				break
		else:
			primes.append(i)

	index = 0
	while index < len(inp):
		num = int(inp[index].rstrip())
		index += 1

		if num == 0:
			break

		people = []
		for i in range(1,num+1):
			people.append(i)

		i = 0
		pindex = 0
		while len(people) > 1:
			pindex = (pindex + primes[i] - 1) % len(people)
			i += 1
			people.pop(pindex)

		print(people[0])

main()