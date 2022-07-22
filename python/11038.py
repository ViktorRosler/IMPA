import sys, math

def calc(num):
	a = str(num)
	cnt = 0
	for i in range(1, len(a)):
		if a[i] == "0":
			cnt += (int(a[0:i])-1) * (10**len(a[i+1:]))
			cnt += 1
			if len(a[i+1:]) > 0:
				cnt += int(a[i+1:]) 
		else:
			cnt += (int(a[0:i])) * (10**len(a[i+1:]))
	return cnt

def main():
	sys.stdin = open('11038.txt', 'r')

	while True:
		init = sys.stdin.readline().split()

		if int(init[0]) < 0:
			return

		a = int(init[0])
		b = int(init[1])

		cnt = 0
		b = calc(b)
		if a > 0:
			a = calc(a-1)
		else:
			b += 1
		
		print(b-a)
		

main()