import sys, math

def main():
	#sys.stdin = open('1753.txt', 'r')

	while True:
		init = sys.stdin.readline().split()

		if init == []:
			break

		sec_nr= int(init[0])
		time = int(init[1])


		bmin = math.inf
		sections = []
		for i in range(sec_nr):
			a = sys.stdin.readline().split()
			sections.append((int(a[0]), int(a[1])))
			bmin = min(int(a[1]), bmin)

		cmin = -bmin
		cmax = 1_001_000

		#print(bmin)

		a = 0
		while abs(cmax - cmin) > 0.000000001:
			a = 0
			cmid = (cmin + cmax) / 2

			for i in sections:
				a += i[0] / (i[1] + cmid)

			if a < time:
				cmax = cmid
			else:
				cmin = cmid

		print("{0:.9f}".format(round(cmax, 9)))			
main()