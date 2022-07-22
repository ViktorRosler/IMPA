import sys

def rec(input, current, index):
	if len(current) == len(input):
		print(current)
		return
	for i in range(len(current)+1):
		rec(input,current[:i] + input[index] + current[i:],index+1)

sys.stdin = open("10063.txt")

for i in range(999999):
	a = sys.stdin.readline().strip()

	if a == "":
		break

	if i > 0:
		print()

	rec(a,"",0)