import sys, math

def factor(num):
	out = []
	while True:	
		for i in range(9, 2, -1):
			if num % i  == 0:
				out.append(i)
				num //= i
				break
		else:
			break
	out.append(num)
	return sorted(out)



def main():
	#sys.stdin = open('10527.txt', 'r')

	while True:
		init = int(sys.stdin.readline())

		if init == -1:
			return
		if init == 0:
			print(10)
			continue

		a = factor(init)
		if len(a) == 1:
			a.insert(0, 1)
		if len(a) > 2:
			while a[0] == 1:
				del a[0]

		if max(a) > 9:
			print("There is no such number.")
		else:
			out = ""
			for i in a:
				out += str(i)
			print(out)


main()