import sys

sys.stdin = open("10029.txt")
alpha = "abcdefghijklmnopqrstuvwxyz"

words = set()
while True:
	a = sys.stdin.readline().strip()
	if a == "":
		break
	words.add(a)

dic = {}
for word in words:
	dic[word] = []
	for i in range(len(word)):
		for letter in alpha:
			if word[i] == letter:
				continue
			new_word = word[:i] + letter + word[i+1:]
			if new_word in words:
				dic[word].append(new_word)

print(dic)