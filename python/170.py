import sys, math

def main():
	#sys.stdin = open('170.txt', 'r')

	while True:
		init = sys.stdin.readline().split()

		if init[0] == "#":
			return

		init.reverse()

		A = [[], [],[], [],[], [],[], [],[], [],[], [],[]]

		for i in range(4):
			if i != 0:
				init = sys.stdin.readline().split()
				init.reverse()
			for j in range(13):
				A[j].insert(0, init[j])

		card = A[12].pop()
		cnt = 1
		while True:
			#print(card, A)
			if card[0] == "T":
				num = 9
			elif card[0] == "J":
				num = 10
			elif card[0] == "Q":
				num = 11
			elif card[0] == "K":
				num = 12
			elif card[0] == "A":
				num = 0
			else:
				num = int(card[0]) - 1

			if len(A[num]) == 0:
				break
			card = A[num].pop()
			cnt += 1
			
		if cnt < 10:
			cnt = "0" + str(cnt)
		print(str(cnt) + "," + str(card))

main()