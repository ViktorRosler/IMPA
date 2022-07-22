import sys, math

def main():
	# sys.stdin = open('10551.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		init = inp[index].rstrip().split()
		index += 1

		if init[0] == '0':
			return

		b = int(init[0])
		p = int(init[1]) 
		m = int(init[2])

		if b != 10:
			decimal_p = 0
			decimal_m = 0
			ps = init[1][::-1]
			ms = init[2][::-1]

			a = 0
			for i in ps:
				decimal_p += int(i) * (b ** a)
				a += 1
			a = 0	
			for i in ms:
				decimal_m += int(i) * (b ** a)
				a += 1
		else:
			decimal_p = p
			decimal_m = m

		ans = int(decimal_p % decimal_m)
		anss = ''
		a = 2
		big = b
		while big < ans:
			big = b ** a
			a += 1

		while True:
			if ans < b:
				while big >= b:
					anss += '0'
					big = int(big / b)
				anss += str(ans)
				break
			else:
				cnt = 0
				while ans >= big:
					ans -= big
					cnt += 1
				anss += str(cnt)
				big = int(big / b)

		print(int(anss))

			

main()