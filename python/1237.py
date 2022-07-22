import sys, math

def main():
	sys.stdin = open('1237.txt', 'r')

	cases = int(sys.stdin.readline())

	for i in range(cases):
		if i != 0:
			print()
		brands = int(sys.stdin.readline())

		arr = []
		for j in range(brands):
			inp = sys.stdin.readline().split()
			arr.append([int(inp[1]), int(inp[2]), inp[0]])

		arr.sort()
		prices = int(sys.stdin.readline())
		for j in range(prices):
			price = int(sys.stdin.readline())
			ans = ""
			done = 1
			for k in range(len(arr)):
				if price < arr[k][0]:
					if ans != "":
						done = 0
						print(ans)
					else:
						done = 0
						print("UNDETERMINED")
					break
				if arr[k][0] <= price <= arr[k][1]:
					if ans == "":
						done = 2
						ans = arr[k][2]
					else:
						done = 0
						print("UNDETERMINED")
						break
			if done == 2:
				print(ans)
			elif done == 1:
				print("UNDETERMINED")


main()