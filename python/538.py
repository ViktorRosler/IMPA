import sys, math

def main():
	sys.stdin = open('538.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	case = 1
	while index < len(inp):
		init = inp[index].rstrip().split()
		index += 1

		if init[0] == init[1] == '0':
			return

		print(f'Case #{case}')
		case += 1

		ppl_nr = int(init[0])
		trades_nr = int(init[1])

		ppl = {}
		for i in range(ppl_nr):
			ppl[inp[index].rstrip()] = 0
			index += 1

		for i in range(trades_nr):
			trade = inp[index].rstrip().split()
			ppl[trade[0]] -= int(trade[2])
			ppl[trade[1]] += int(trade[2])
			index += 1

		pos = []
		neg = []
		for i in ppl:
			if ppl[i] > 0:
				pos.append(i)
			else:
				neg.append(i)

		while pos:
			plus = ppl[pos[0]]
			minus = ppl[neg[0]]

			if plus + minus == 0:
				print(f'{pos[0]} {neg[0]} {plus}')
				del pos[0]
				del neg[0]
			elif plus + minus > 0:
				print(f'{pos[0]} {neg[0]} {-minus}')
				del neg[0]
				ppl[pos[0]] += minus
			elif plus + minus < 0:
				print(f'{pos[0]} {neg[0]} {plus}')
				del pos[0]
				ppl[neg[0]] += plus
		print()


main()