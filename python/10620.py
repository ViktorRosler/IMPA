import sys, math

# return true if on white square
def wb(S, x, y):
	a = False

	if x > S:
		t = x // S
		x -= S * t
		if t % 2 == 1:
			a = not a

	if x == S or x == 0:
		return False 

	if y > S:
		t = y // S
		y -= S * t
		if t % 2 == 1:
			a = not a

	if y == S or y == 0:
		return False

	return a

def done(x, y, jumps, failed):
	if failed:
		print('The flea cannot escape from black squares.')
	else:
		print('After {} jumps the flea lands at ({}, {}).'.format(jumps, x, y))


def main():
	sys.stdin = open('10620.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		init = inp[index].rstrip().split()
		index += 1

		S = int(init[0])

		if S == 0:
			return

		x = int(init[1])
		y = int(init[2])
		dx = int(init[3])
		dy = int(init[4])
		jumps = 0


		a = (S // math.gcd(S, dx)) * (S // math.gcd(S, dy))
		print(a)
		b = True
		for i in range(a+1):
			if wb(S, x, y):
				done(x, y, jumps, False)
				b = False
				break
			x += dx
			y += dy
			jumps += 1

		if b:
			done(x, y, jumps, True)


main()