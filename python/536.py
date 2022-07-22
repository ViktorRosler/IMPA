import sys, math

root_left_right = None
# (root, left, right)
def create_tree(string):
	global root_left_right

	if len(string) == 0:
		return None
	if len(string) == 1:
		root_left_right = root_left_right[1:]
		return (string, None, None)

	root = root_left_right[0]
	root_left_right = root_left_right[1:]
	root_index = string.index(root)

	return(root, create_tree(string[:root_index]), create_tree(string[root_index+1:]))

def postorder(tree):
	if tree == None:
		return ''
	else:
		return postorder(tree[1]) + postorder(tree[2]) + tree[0]

def main():
	# sys.stdin = open('536.txt', 'r')
	inp = sys.stdin.readlines()

	index = 0
	while index < len(inp):
		init = inp[index].rstrip().split(' ')
		index += 1

		global root_left_right
		root_left_right = init[0]

		left_root_right = init[1]

		tree = create_tree(left_root_right)
		print(postorder(tree))

main()