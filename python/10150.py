import sys, math

def main():
	#sys.stdin = open('10150.txt', 'r')

	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
	'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


	d = set()
	while True:
		init = sys.stdin.readline().strip()
		if init == '':
			break
		d.add(init)


	first_case = True
	while True:
		init = sys.stdin.readline().split()
		if len(init) == 0:
			break

		word1 = init[0]
		word2 = init[1]

		todo = [word2]
		done = set()
		done.add(word2)
		done_dict = {}
		depth = 0
		not_done = True
		solution = False
		while not_done:
			depth += 1
			not_done = False
			for word in todo[:]:
				todo.pop(0)
				for i in range(len(word)):
					for l in letters:
						new_word = word[:i] + l + word[i+1:]
						if new_word in done or new_word not in d:
							continue
						not_done = True
						if new_word == word1:
							solution = True
							not_done = False

						todo.append(new_word)
						done.add(new_word)
						done_dict[new_word] = word


		if not first_case:
			print()
		first_case = False

		if solution:
			print(word1)
			while True:
				word1 = done_dict[word1]
				print(word1)
				if word1 == word2:
					break
		else:
			print('No solution.')
		



main()