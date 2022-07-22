import sys, math

def func(subs,marks,dp):
	if (subs,marks) in dp:
		return(dp[(subs,marks)])
	if marks == 0:
		dp[(subs,marks)] = 1
		return 1
	if marks == 1:
		dp[(subs,marks)] = subs
		return subs
	if subs == 0:
		dp[(subs,marks)] = 0
		return 0
	if subs == 1:
		dp[(subs,marks)] = 1
		return 1


	ans = 0
	for i in range(marks+1):
		ans += func(subs-1,marks-i,dp)

	dp[(subs,marks)] = ans
	return ans
   


def main():
	sys.stdin = open('10910.txt', 'r')

	cases = int(sys.stdin.readline())

	for c in range(cases):
		init = sys.stdin.readline().split()

		N = int(init[0])
		T = int(init[1])
		P = int(init[2])

		A = T - P*N # 4
		B = N-1     # 2

		dp = {}
		ans = func(N,A,dp)

		print(ans)





main()