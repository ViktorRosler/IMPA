import sys, math


def prim_fact(num, primes):
	out = []
	while num > 1:	
		for i in primes:
			if num % i == 0:
				out.append(i)
				num /= i
				break
		else:
			out.append(int(num))
			break

	return out

def main():
	# sys.stdin = open('10042.txt', 'r')
	inp = sys.stdin.readlines()

	primes = []
	for i in range(2, 32000):
		for j in range(2, int(math.sqrt(i)+1)):
			if i % j == 0:
				break
		else:
			primes.append(i)

	index = 1
	while index < len(inp):
		num = int(inp[index].rstrip()) + 1
		index += 1

		while True:
			s = str(num)
			num_sum = 0
			for i in s:
				num_sum += int(i)

			prim_sum = 0
			p = prim_fact(num, primes)

			if len(p) == 1:
				num += 1
				continue

			for i in p:
				if i > 9:
					tmp = str(i)
					for j in tmp:
						prim_sum += int(j)
				else:
					prim_sum += i

			if num_sum == prim_sum:
				break
			else:
				num += 1

		print(num)

main()