import sys, math

def main():
	#sys.stdin = open('10668.txt', 'r')

	while True:
		init = sys.stdin.readline().split()

		if int(init[0]) < 0:
			return

		L = float(init[0])
		n = float(init[1]) 
		C = float(init[2])

		L2 = (1 + n*C) * L

		if (L2 == L):
			print("0.000")
			continue

		left = 0
		right = 4
		for i in range(1, 1000):
			angle = (left + right) / 2
			R =  L / (2 * math.sin(angle / 2))
			guess = R * angle
			
			if guess > L2:
				right = angle
			else:
				left = angle


		angle = (left + right) / 2	
		R =  L / (2 * math.sin(angle / 2))	
		ans = R * (1 - math.cos(angle / 2))
		print("{:.3f}".format(ans))

main()