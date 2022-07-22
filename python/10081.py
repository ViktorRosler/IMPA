import sys, math

def main():
	sys.stdin = open('10081.txt', 'r')

	while True:
		init = sys.stdin.readline().split()

		if len(init) == 0:
			return

		k = int(init[0]) + 1
		n = int(init[1])

		if k < 3 or n == 1:
			print("100.00000")
			continue

		cnt = 0
		pair = (2*(k-2) + (k-2)*(k-3)) / k**2
		#print(pair)
		# neighbours * [one of the numbers are 0 or k] * [other number is not close to 0 or k] * [the other parts of the word can be anything]
		cnt +=  pair * (n-1)
			

		print((k**n - cnt) / k**n)


main()