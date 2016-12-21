'''
Mirroring a binary tree


   1                1
  / \              / \
 2   3     =>     3   2
  \                  /
   4                4

'''
tree = [1,[2,[],[4,[],[]]],[3,[],[]]]
def mirror(root):
	if root==[]:
		return 
	mirror(root[1])
	mirror(root[2])
	root[1],root[2] = root[2],root[1]

mirrir(tree)
print(tree)
