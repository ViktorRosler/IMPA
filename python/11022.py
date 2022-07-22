import sys, math

# check if whole (sub)string can be factored and if so return factor length
def find_fact_length(string):
	length = len(string)
	for i in range(1, length):
		if length % i == 0:
			if string[:i] * (length // i) == string:
				return i

# recursivly find shortest factoring
def solve(dp, string):

	if string in dp:
		return dp[string]
	elif len(string) == 1:
		return 1

	length = 0
	fact = find_fact_length(string)
	# if the whole string can be factored
	if fact != None:
		length = solve(dp, string[:fact])

	# recursivly find the shortest factoring of two substrings sub1 sub2 such that: string = sub1 + sub2
	if length == 0:
		length = min([solve(dp, string[:i+1]) + solve(dp, string[i+1:]) for i in range(len(string)-1)])

	dp[string] = length
	return length

def main():
	sys.stdin = open('11022.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		
		string = inp[index].rstrip()
		index += 1

		if string == '*':
			return

		# dynamic programming, inte double penetration
		dp = {}

		print(solve(dp, string))


main()