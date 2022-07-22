import sys, math

def main():
	#sys.stdin = open('10997.txt', 'r')

	while True:
		init = int(sys.stdin.readline())

		if init == 0:
			return

		countries = []
		total = 0
		for i in range(init):
			a = sys.stdin.readline().split()
			if a[0] == 'Canada':
				canada = (int(a[1]), int(a[2]), int(a[3]))
			else:
				countries.append((int(a[1]), int(a[2]), int(a[3])))
			total += int(a[1]) + int(a[2]) + int(a[3])

		done = False
		for i in range(-3,4):
			for j in range(-3,4):
				for k in range(-3,4):
					b = (total**i, total**j, total**k)
					for land in countries:
						if land[0]*b[0] + land[1]*b[1] + land[2]*b[2] >= canada[0]*b[0] + canada[1]*b[1] + canada[2]*b[2]:
							break
					else:
						print('Canada wins!')
						done = True
					if done:
						break
				if done:
					break
			if done:
				break

		if not done:
			print('Canada cannot win.')


main()