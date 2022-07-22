import sys, math

''' SEQUENCES '''
A = '''0'''    # 0     Length 1

B = '''1'''    # 1     Length 1

C = '''02'''   # A2    Length 2

D = '''1003''' # BAA3  Length 4

E = '''02110004''' # CBBAAA4     Length 8

F = '''1003020211100005'''  # DCCBBBAAAA5     Length 16

G = '''02110004100310030202021111000006''' # EDDCCCBBBBAAAAA6     Length 32

H = '''1003020211100005021100040211000410031003100302020202111110000007''' # FEEDDDCCCCBBBBBAAAAAA7     Length 64

I = '''02110004100310030202021111000006100302021110000510030202111000050211000402110004021100041003100310031003020202020211111100000008'''

J = '''1003020211100005021100040211000410031003100302020202111110000007021100041003100302020211110000060211000410031003020202111100000610030202111000051003020211100005100302021110000502110004021100040211000402110004100310031003100310030202020202021111111000000009'''

K = '''021100041003100302020211110000061003020211100005100302021110000502110004021100040211000410031003100310030202020202111111000000081003020211100005021100040211000410031003100302020202111110000007100302021110000502110004021100041003100310030202020211111000000702110004100310030202021111000006021100041003100302020211110000060211000410031003020202111100000610030202111000051003020211100005100302021110000510030202111000050211000402110004021100040211000402110004100310031003100310031003020202020202021111111100000000010'''

def Hen(string):
	out = ''
	for c in string:
		out += int(c) * '0' + str(int(c)+1)
	return out


def main():
	# sys.stdin = open('10479.txt', 'r')
	inp = sys.stdin.readlines()

	# lista med längden av rader
	row_length = [1,1]
	for i in range(1,65):
		row_length.append(2 ** i)

	index = 0
	while index < len(inp):
		num = int(inp[index].rstrip())
		index += 1

		if num == 0:
			return

		# ta bort längden av alla rader upp till raden num finns på
		for i in range(1,65):
			if num < 2 ** i:
				num -= 2 ** (i-1)
				rad = i
				break

		# när num är sista talet i en rad
		if num == 0:
			print(rad-1)
			continue

		while num > 0:

			# när num finns i rad 1 eller rad 2
			if rad == 0:
				print(0)
				break
			if rad == 1:
				print(1)
				break

			delrad_summa = 0
			delrad = rad-2
			delrad_antal = 1

			# hitta vilken delrad i raden num finns i, t.ex i D 
			while delrad >= 0:
				if delrad_summa + row_length[delrad] * delrad_antal >= num:
					break
				else:
					delrad_summa += row_length[delrad] * delrad_antal
				delrad -= 1
				delrad_antal += 1
			num -= delrad_summa

			# hitta vilket index num finns på i delraden, t.ex. var i D
			while delrad_antal > 0 and num >= row_length[delrad]:
				num -= row_length[delrad]
				delrad_antal-= 1

			# när rätt plats har hittats
			if num == 0:
				print(delrad)

			rad = delrad

main()