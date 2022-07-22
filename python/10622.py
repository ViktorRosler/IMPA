import sys, math

def search(b, t, mult, init):
	bot = b
	top = t
	mid = (bot + top) // 2
	while top >= bot:
		num = mid ** mult
		if 	num == init:
			return True
		elif num > init:
			top = mid - 1
			mid = (bot + top) // 2
		elif num < init:
			bot = mid + 1
			mid = (bot + top) // 2
	return False


def main():
	# sys.stdin = open('10622.txt', 'r')
	inp = sys.stdin.readlines()

	big_int = 2_147_483_647
	big_squared = 46340

	index = 0
	while index < len(inp):
		init = int(inp[index].rstrip())
		index += 1

		if init == 0:
			return

		step = -1
		if init < 0:
			init *= -1
			step = -2

		# dp = {12:8, 16:7, 23:6, 37:5, 75:4, 217:3, 1292:2, 46340:1}
		ans = 1
		for i in range(31,1,step):
			if search(2, big_squared, i, init):
				ans = i
				break
		print(ans)


		




	


main()