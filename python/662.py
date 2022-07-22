import sys, math
from collections import deque

def mid_ele(lst):
	max_d = lst[-1] - lst[0]
	mid_ele = lst[0]
	for i in range(1, len(lst) - 1):
		a = lst[i] - lst[0]
		b = lst[-1] - lst[i]
		if a < max_d and b < max_d:
			max_d = max(a,b)
			mid_ele = lst[i]
	return mid_ele

def max_dist(lst):
	max_d = lst[-1] - lst[0]
	for i in range(1, len(lst) - 1):
		a = lst[i] - lst[0]
		b = lst[-1] - lst[i]
		if a < max_d and b < max_d:
			max_d = max(a,b)
	return max_d

def main():
	sys.stdin = open('662.txt', 'r')

	chain = 1
	while True:
		init = sys.stdin.readline().split()
		n = int(init[0])
		k = int(init[1])
		if n == 0 and k == 0:
			return
		offset = n // k
		seq = []
		for i in range(n):
			seq.append(int(sys.stdin.readline()))


		if len(seq) == 1:
			print("Chain", chain)
			chain += 1
			print("Depot", 1, "at restaurant", 1, "serves restaurant", 1)
			print("Total distance sum =", 0)
			print()
			continue

		l = []
		ind = 0
		for i in range(k):
			l.append([])
			for j in range(offset):
				l[-1].append(seq[ind])
				ind += 1
		while ind < n:
			l[-1].append(seq[ind])
			ind += 1
		
		to_beat = 0
		for i in l:
			if i[-1] - i[0] > to_beat:
				to_beat = i[-1] - i[0]

		solution = l
		while True:
			l2 = []
			ind = len(seq) - 1
			for i in range(k):
				l2.insert(0, [])
				l2[0].insert(0, seq[ind])
				ind -= 1
				while ind >= 0 and max_dist([seq[ind]] + l2[0]) < to_beat:
					l2[0].insert(0, seq[ind])
					ind -= 1
				if ind < 0:
					c = []
					for j in l2:
						c.append(max_dist(j))
					solution = l2
					to_beat = max(c)
					break
			if ind != -1 or to_beat == 0:
				break

		#print(solution)
		print("Chain", chain)
		chain += 1
		total = 0
		ind = 1
		for i in solution:
			a = mid_ele(i)
			if len(i) == 1:
				print("Depot", ind, "at restaurant", seq.index(a) + 1, "serves restaurant", seq.index(i[0]) + 1)
			else:
				print("Depot", ind, "at restaurant", seq.index(a) + 1, "serves restaurants", seq.index(i[0]) + 1, "to", seq.index(i[-1]) + 1)
			ind += 1
			for j in i:
				if j < a:
					total += a-j
				else:
					total += j-a

		print("Total distance sum =", total)
		print()
			

main()