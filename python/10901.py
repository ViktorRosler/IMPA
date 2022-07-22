import sys, math

def main():
	#sys.stdin = open('10901.txt', 'r')

	cases = int(sys.stdin.readline())


	for i in range(cases):
		init = sys.stdin.readline().split()

		capacity = int(init[0])
		pass_time = int(init[1])
		lines = int(init[2])

		side = "left"
		left = []
		right = []
		for j in range(lines):
			a = sys.stdin.readline().split()
			if a[1] == "left":
				left.append((int(a[0]),j))
			else:
				right.append((int(a[0]),j))

		time = 0
		carry = 0
		out = {}
		while len(left) != 0 or len(right) != 0:
			if side == "left":
				while True:
					if len(left) > 0 and time >= left[0][0] and carry < capacity:
						carry += 1
						out[left[0][1]] = time + pass_time
						del left[0]
					else:
						break
				if carry > 0 or (len(right) > 0 and time >= right[0][0]):
					side = "right"
					time += pass_time
					carry = 0
				else:
					time += 1
			elif side == "right":
				while True:
					if len(right) > 0 and time >= right[0][0] and carry < capacity:
						carry += 1
						out[right[0][1]] = time + pass_time
						del right[0]
					else:
						break
				if carry > 0 or (len(left) > 0 and time >= left[0][0]):
					side = "left"
					time += pass_time
					carry = 0
				else:
					time += 1
		if i > 0:
			print()
		for j in range(lines):
			print(out[j])
		



main()