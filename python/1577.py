import sys, math

def main():
	sys.stdin = open('1577.txt', 'r')
	init = sys.stdin.readlines()
	index = 0
	cnt = 0
	while index < len(init):
		a,b = init[index].split()
		index += 1

		machines = int(a)
		batteries = int(b)
		power = []
		for i in init[index].split():
			power.append((int(i)))
		index += 1

		power = sorted(power)
		for i in range(2 * (batteries - 1)):
				del power[-1]

		cnt += 1
		if cnt == 36:
			print(power)

		deletable = 0
		least = 0
		todo = machines

		for i in range(machines):
			while deletable > 0:
				power2 = power[:]

				for j in range(todo - 1):
					d = math.inf
					index2 = 1
					for k in range(1, len(power2)):
						if power2[k] - power2[k-1] < d:
							d = power2[k] - power2[k-1]
							index2 = k
					del power2[index2]
					del power2[index2 - 1]

				c = math.inf
				for j in range(1, len(power2)):
					if power2[j] - power2[j-1] < c:
						c = power2[j] - power2[j-1]

				a = power[1] - power[0]	
				if a <= c:
					break

				
				for j in range (1, deletable+1):
					if power[j+1] - power[j] < a:
						print(power[0], " b")
						del power[0]
						deletable -= 1
						break
				else:
					break


			if power[1] - power[0] > least:
				least = power[1] - power[0]

			del power[0]
			del power[0]

			todo -= 1
			deletable += 2 * (batteries - 1)

		print(least)


		






main()