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
	# sys.stdin = open('10139.txt', 'r')
	inp = sys.stdin.readlines()

	primes = []
	for i in range(2, 47000):
		for j in range(2, int(math.sqrt(i)+1)):
			if i % j == 0:
				break
		else:
			primes.append(i)

	# print(primes)

	index = 0
	while index < len(inp):
		init = inp[index].rstrip().split(' ')
		index += 1

		a = int(init[1])
		b = prim_fact(a, primes)

		divides = True
		# print(b)
		
		for i in range(len(b)):
			if i == 0 or b[i] != b[i-1]:
				count = b.count(b[i])
				count2 = 0
				for j in range(b[i], int(init[0])+1, b[i]):
					if count2 >= count:
						break
					temp = j
					while temp % b[i] == 0:
						count2 += 1
						temp /= b[i]
				if count > count2:
					divides = False
					break	
				
		if divides:
			print('{} divides {}!'.format(init[1], init[0]))
		else:
			print('{} does not divide {}!'.format(init[1], init[0]))

main()