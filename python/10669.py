import sys, math

def main():
	#sys.stdin = open('10669.txt', 'r')

	while True:
		init = int(sys.stdin.readline())

		if init == 0:
			return

		num = []
		while init > 1:
			n = 0
			while 2**(n+1) < init:
				n += 1
			num.insert(0, 3**n)
			init -= 2**n
	
		print('{', end='')
		for i in num:
			if i == num[0]:
				print(' ', end='')
			else:
				print(', ', end='')
			print(i, end='')
		print(' }')




main()