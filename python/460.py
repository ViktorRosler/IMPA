import sys, math

def main():
	sys.stdin = open('460.txt', 'r')

	cases = int(sys.stdin.readline())
	
	for i in range(cases):
		w1 = []
		w2 = []

		while len(w1) < 4:
			w1 = sys.stdin.readline().split()

		while len(w2) < 4:
			w2 = sys.stdin.readline().split()

		w1 = [int(w1[0]), int(w1[1]), int(w1[2]), int(w1[3])]
		w2 = [int(w2[0]), int(w2[1]), int(w2[2]), int(w2[3])]

		x1 = 0
		x2 = 0
		y1 = 0
		y2 = 0

		if i > 0:
			print()

		if w1[0] < w2[0]:
			if w1[2] <= w2[0]:
				print("No Overlap")
				continue
			else:
				x1 = w2[0]
				x2 = min(w1[2], w2[2])
		else:
			if w2[2] <= w1[0]:
				print("No Overlap")
				continue
			else:
				x1 = w1[0]
				x2 = min(w2[2], w1[2])


		if w1[1] <= w2[1]:
			if w1[3] < w2[1]:
				print("No Overlap")
				continue
			else:
				y1 = w2[1]
				y2 = min(w1[3], w2[3])
		else:
			if w2[3] <= w1[1]:
				print("No Overlap")
				continue
			else:
				y1 = w1[1]
				y2 = min(w2[3], w1[3])

		if x1 == x2 or y1 == y2:
			print("No Overlap")
		else:
			print(x1, y1, x2, y2)

main()