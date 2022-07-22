import sys

sys.stdin = open("11201.txt")

odd_letters = "bcdfghjklmnpqrstvwxyz"
even_letters = "aeiou"

dic = {}
dic['a'] = 12.53
dic['b'] = 1.42
dic['c'] = 4.68
dic['d'] = 5.86
dic['e'] = 13.68
dic['f'] = 0.69
dic['g'] = 1.01
dic['h'] = 0.7
dic['i'] = 6.25
dic['j'] = 0.44
dic['k'] = 0.00
dic['l'] = 4.97
dic['m'] = 3.15
dic['n'] = 6.71
dic['o'] = 8.68
dic['p'] = 2.51
dic['q'] = 0.88
dic['r'] = 6.87
dic['s'] = 7.98
dic['t'] = 4.63
dic['u'] = 3.93
dic['v'] = 0.9
dic['w'] = 0.02
dic['x'] = 0.22
dic['y'] = 0.9
dic['z'] = 0.52

average_odd = 0
for i in odd_letters:
	average_odd += dic[i]
average_odd /= len(odd_letters)

average_even = 0
for i in even_letters:
	average_even += dic[i]
average_even /= len(even_letters)

# print(average_even, average_odd)

average_costs = {}
for j in odd_letters + even_letters:
	average_costs[j] = [dic[j]]
	s = dic[j]
	for i in range(2, 100):
		if i % 2 == 0:
			s += average_even * i
		else:
			s += average_odd * i
		average_costs[j].append(s)

words = int(sys.stdin.readline())

for i in range(words):
	a = sys.stdin.readline().strip()
	t = 0
	for j in range(1, len(a)+1):
		t += dic[a[j-1]] * j
	if t >= average_costs[a[0]][len(a)-1]:
		print("above or equal")
	else:
		print("below")