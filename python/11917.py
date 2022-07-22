import sys


#sys.stdin = open('11917.txt', 'r')

cases = int(sys.stdin.readline())

for i in range(cases):
	sub = int(sys.stdin.readline())
	subs = {}
	for j in range(sub):
		a = sys.stdin.readline().split()
		subs[a[0]] = int(a[1])
	d = int(sys.stdin.readline())
	sub = sys.stdin.readline().strip()

	if sub not in subs:
		print("Case {0}: Do your own homework!".format(i+1))
	elif subs[sub] <= d:
		print("Case {0}: Yesss".format(i+1))
	elif subs[sub] <= d+5:
		print("Case {0}: Late".format(i+1))
	else:
		print("Case {0}: Do your own homework!".format(i+1))