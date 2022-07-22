import sys, math

def main():
	#sys.stdin = open('10038.txt', 'r')

	while True:
		init = sys.stdin.readline().split()

		if init == []:
			break

		diff = []
		for i in range(2,len(init)):
			diff.append(abs(int(init[i]) - int(init[i-1])))

		diff.sort()

		jolly = True
		for i in range(1, len(diff)+1):
			if i != diff[i-1]:
				jolly = False

		if jolly:
			print("Jolly")
		else:
			print("Not jolly")

main()