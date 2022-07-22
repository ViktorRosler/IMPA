import sys

def check(s):
	for i in range(1,len(s)):
		for j in range(len(s)-i):
			if s[j:j+i] == s[j+i:j+i+i]:
				return False
	return True

sys.stdin = open("129.txt", 'r')

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

dic = {}
dic["A"] = ["A"]
dic["AB"] = ["A", "AB", "ABA", "B", "BA", "BAB"]

while True:
	a = sys.stdin.readline().split()

	if a[0] == "0" and a[1] == "0":
		break

	b = int(a[0])
	c = int(a[1])
	d = s[:c]
	if d not in dic:
		dic[d] = []
		t = ""
		while len(dic[d]) < 90:
			f = False
			for i in d:
				if check(t + i):
					t += i
					f = True
					dic[d].append(t)
					break
			if f:
				continue
			for i in d:
				if t[:-1] + i != t and check(t[:-1] + i):
					t = t[:-1] + i
					dic[d].append(t)
					f = True
					break
			if f:
				continue
			for i in d:
				if t[-2] != i and check(t[:-2] + i):
					t = t[:-2] + i
					dic[d].append(t)
					break
				if t[-2] != i and check(t[:-2] + i):	
					t = t[:-2] + i
					dic[d].append(t)
					break
				if t[-2] != i and check(t[:-2] + i):	
					t = t[:-2] + i
					dic[d].append(t)
					break						
	e = dic[d][b-1]
	f = len(e)
	g = []
	i = 0
	while i < f:
		if i+4 > f:
			g.append(e[i:])
		else:
			g.append(e[i:i+4])
		i += 4
	for i in range(1, len(g)+1):
		if i == 17:
			print()
		elif i > 1:
			print(" ", end="")
		print(g[i-1], end="")
	print()
	print(f)


