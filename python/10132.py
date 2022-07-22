import sys

sys.stdin = open("10132.txt", 'r')

cases = int(sys.stdin.readline())
sys.stdin.readline()

for i in range(cases):
	dic = {}
	cnt = 0
	s = 0
	while True:
		b = sys.stdin.readline().strip()

		if b == "":
			break

		cnt += 1
		s += len(b)

		if len(b) not in dic:
			dic[len(b)] = []

		dic[len(b)].append(b)

	c = s*2 // cnt

	dic2 = {}
	for y in range(1, (c // 2) + 1):
		if y in dic:
			for j in dic[y]:
				for k in dic[c-y]:
					f = j+k
					if f not in dic2:
						dic2[f] = 1
					else:
						dic2[f] += 1
	ans, m = "", 0					
	for key,val in dic2.items():
		if val > m:
			m = val
			ans = key
	if i > 0:
		print()
	print(ans)