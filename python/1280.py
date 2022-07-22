import sys, math

def main():
	#sys.stdin = open('1280.txt', 'r')

	case = 0
	while True:
		case += 1
		init = sys.stdin.readline()

		if init == "":
			break

		degree = int(init)
		coeff = sys.stdin.readline().split()
		for i in range(degree+1):
			coeff[i] = float(coeff[i])

		init = sys.stdin.readline().split()

		xmin = float(init[0])
		org_min = xmin
		xmax = float(init[1])
		step = int(init[2])

		summa = 0
		part_sum = 0
		steps = 0
		step_arr = []
		while xmin < xmax:
			r = coeff[0]
			for i in range(1,degree+1):
				r += coeff[i] * (xmin ** i)
			a = math.pi * (r ** 2) * 0.00004
			summa += a
			if steps < 8:
				part_sum += a
				if part_sum >= step:
					steps += 1
					step_arr.append(xmin-org_min)
					part_sum -= step
			xmin += 0.00004
			


		print("Case {0}: {1:.2f}".format(case,summa))
		if len(step_arr) == 0:
			print("insufficient volume")
		else:
			s = ""
			for i in range(len(step_arr)):
				if i > 0:
					s += " "
				s += "{0:.2f}".format(step_arr[i])
			print(s)

main()