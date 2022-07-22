import sys, math

def main():
	sys.stdin = open('10550.txt', 'r')

	while True:
		init = sys.stdin.readline().split()

		if init[0] == init[1] == init[2] == init[3] == '0':
			break
		start = int(init[0])
		first = int(init[1])
		snd = int(init[2])
		thrd = int(init[3])

		ans = 1080

		if start < first:
			start += 40
		ans += (start - first) * 9

		tmp = snd
		if tmp < first:
			tmp += 40
		ans += (tmp - first) * 9

		if snd < thrd:
			snd += 40
		ans += (snd - thrd) * 9

		print(ans)

main()