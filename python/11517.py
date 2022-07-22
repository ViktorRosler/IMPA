import sys, math

def main():
	sys.stdin = open('11517.txt', 'r')

	init = int(sys.stdin.readline())

	while init > 0:
		init -= 1;
		price = int(sys.stdin.readline())
		bills = int(sys.stdin.readline())
	

		dp = {}
		amount = {}
		for i in range(10010):
			dp[i] = -1
			amount[i] = 0

		dp[0] = 0

		while bills > 0:
			bills -= 1
			bill = int(sys.stdin.readline())

			for i in range(price, 0, -1):
				idx = i - bill
				if idx >= 0:
				
					if dp[idx] != -1:
						now = dp[idx] + bill
						use = amount[idx] + 1
						if now < dp[i] or dp[i] == -1:
							dp[i] = now
							amount[i] = use
						elif now == dp[i] and amount[i] > use:
							amount[i] = use
				
				elif dp[i] == -1 or dp[i] >= bill:
				
					dp[i] = bill
					amount[i] = 1

		print(dp[price], amount[price])
				

		

main()