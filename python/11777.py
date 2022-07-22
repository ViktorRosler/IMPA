import sys, math

def main():
	sys.stdin = open('11777.txt', 'r')

	cases = int(sys.stdin.readline())

	for i in range(cases):
		init = sys.stdin.readline().split()

		a = int(init[0]) + int(init[1]) + int(init[2]) + int(init[3])

		if int(init[5]) >= int(init[4]) and int(init[6]) >= int(init[4]):
			a += (int(init[5]) +  int(init[6])) / 2
		elif int(init[4]) >= int(init[5]) and int(init[6]) >= int(init[5]):
			a += (int(init[4]) +  int(init[6])) / 2
		else:
			a += (int(init[4]) +  int(init[5])) / 2


		if a >= 90:
			print("Case {0}: A".format(i+1))
		elif a >= 80:
			print("Case {0}: B".format(i+1))
		elif a >= 70:
			print("Case {0}: C".format(i+1))
		elif a >= 60:
			print("Case {0}: D".format(i+1))
		else:
			print("Case {0}: F".format(i+1))
main()