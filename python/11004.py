import sys, math

def main():
	# sys.stdin = open('11004.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	count = 0
	while index < len(inp):
		roads_nr = int(inp[index].rstrip())
		index += 1
		count += 1

		if roads_nr == 0:
			return

		roads = []
		for i in range(roads_nr):
			r = inp[index].rstrip().split()
			index += 1
			roads.insert(0,(int(r[0]),int(r[1]),int(r[2])))

		PP_nr = int(inp[index].rstrip())
		index += 1

		PP = []
		for i in range(PP_nr):
			p = inp[index].rstrip().split()
			index += 1
			PP.insert(0,(int(p[0]),int(p[1])))


		'''
		 k<0 om eq för båda vägarna har samma tecken i punkten
		-> hitta antalet par av vägar som har samma tecken
		-> med hjälp av formeln för aritmetisk summa '''
		ans = 0
		for p in PP:
			pos = 0
			neg = 0
			for i in roads:
				if i[0]*p[0]+i[1]*p[1]+i[2] > 0:
					pos += 1
				else:
					neg += 1
			ans += pos*(pos-1)/2
			ans += neg*(neg-1)/2
						
		print('Roadmap {}:'.format(count))
		print('Negative Builders Ltd. will build {} New Roads.'.format(int(ans)))


main()