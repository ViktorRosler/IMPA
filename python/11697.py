import sys, math

def main():
	sys.stdin = open('11697.txt', 'r')

	cases = int(sys.stdin.readline())

	for i in range(cases):
	
		phrase = sys.stdin.readline().strip()

		key = []
		dic = {}

		for i in phrase:
			if i not in key and i != " ":
				key.append(i)
				dic[i] = len(key)

		for i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']:
			if i not in key:
				key.append(i)
				dic[i] = len(key)

		line = sys.stdin.readline().strip()

		arr = []
		dbl = ""
		for i in range(len(line)):

			if line[i] == " ":
				continue

			dbl += line[i]
			if len(dbl) == 2:
				if dbl[0] == dbl[1]:
					arr.append(dbl[0] + 'x')
					dbl = dbl[1]
				else:
					arr.append(dbl)
					dbl = ""
					continue

			if  i == len(line) - 1:
				if len(dbl) == 1:
					dbl += 'x'
				arr.append(dbl)


		out = ""
		for i in arr:
			if (dic[i[0]]-1) // 5 == (dic[i[1]]-1) // 5:

				if dic[i[0]] % 5 == 0:
					out += key[dic[i[0]]-5].upper()
				else:
					out += key[dic[i[0]]].upper()

				if dic[i[1]] % 5 == 0:
					out += key[dic[i[1]]-5].upper()
				else:
					out += key[dic[i[1]]].upper()

			elif dic[i[0]] % 5 == dic[i[1]] % 5:
				out += key[(dic[i[0]]+4) % 25].upper()
				out += key[(dic[i[1]]+4) % 25].upper()

			else:
				a = dic[i[1]] % 5
				if a == 0:
					a = 5
				b = dic[i[0]] % 5
				if b == 0:
					b = 5
				out += key[dic[i[0]]+a-b-1].upper()

				a = dic[i[0]] % 5
				if a == 0:
					a = 5
				b = dic[i[1]] % 5
				if b == 0:
					b = 5
				out += key[dic[i[1]]+a-b-1].upper()

		print(out)


main()