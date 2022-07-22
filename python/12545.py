import sys, math

def main():
	#sys.stdin = open('12545.txt', 'r')
	inp = sys.stdin.readlines()

	index = 1
	case = 1
	while index < len(inp):
		S = inp[index].rstrip()
		index += 1

		T = inp[index].rstrip()
		index += 1

		m = 0
		while S != T:
			s = (S.count('0'), S.count('1'), S.count('?'))
			t = (T.count('0'), T.count('1'))

			if t[0] > s[0]:
				if s[2] > 0:
					cnt = 0
					for i in range(len(S)):
						if S[i] == '?':
							cnt += 1
							if T[i] == '0' or cnt == s[2]:
								S = S[:i] + '0' + S[i+1:]
								m += 1
								break
				else:
					m = -1
					break


			elif s[2] > 0:
				i = S.index('?')
				S = S[:i] + '1' + S[i+1:]
				m += 1

			elif s[1] == t[1]:
				for i in range(len(S)):
					if S[i] != T[i]:
						for j in range(i+1, len(S)):
							if S[i] != S[j] and S[j] != T[j]:
								S = S[:i] + S[j] + S[i+1:j] + S[i] + S[j+1:]
								m += 1
								break

			else:
				for i in range(len(S)):
					if S[i] == '0' and T[i] == '1':
						S = S[:i] + '1' + S[i+1:]
						m += 1
						break


		print('Case {}:'.format(case), end=' ')
		print(m)
		case += 1


main()