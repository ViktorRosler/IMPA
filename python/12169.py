import sys, math

def main():
	sys.stdin = open('12169.txt', 'r')

	cases = int(sys.stdin.readline())

	index = 0
	arr = []
	while index < cases:
		index += 1
		init = int(sys.stdin.readline())
		arr.append(init)

	ra = 0
	rb = 0
	for a in range(10001):
		for b in range(10001):
			x = arr[0]
			done = True
			for n in range(len(arr)):
				if x != arr[n]:
					done = False
				x = (a * x + b) % 10001
				x = (a * x + b) % 10001
			if done:
				ra = a
				rb = b
				break
		if done:
			break

	for n in range(len(arr)):
		print((ra * arr[n] + rb) % 10001)


main()