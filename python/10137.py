import sys, math

def main():
	# sys.stdin = open('10137.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		num = int(inp[index].rstrip())
		index += 1

		if num == 0:
			return

		costs = []
		avg = 0
		for i in range(num):
			costs.append(float(inp[index].rstrip()))
			index += 1
			avg += costs[i]

		avg = round(avg/num, 2)


		t1 = 0
		t2 = 0
		for i in costs:
			if i > avg:
				t1 += i - avg
			if avg > i:
				t2 += avg - i

		if t2 < t1:
			t1 = t2

		print('${:.2f}'.format(t1))

main()