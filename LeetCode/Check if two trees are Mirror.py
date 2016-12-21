'''
Check if two trees are Mirror

   A                B
   
   1                1
  / \              / \
 2   3      ,     3   2   => True
  \                  /
   4                4


   A                B
   
   1                1
  / \              / \
 2   3      ,     3   2   => False
  \                    \
   4                    4        


Given two Binary Trees, write a function that returns true if two trees are mirror of each other,
else false. For example, the function should return true for following input trees.

'''

a =[1,[2,None,[4,None,None]],[3,None,None]]
b =[1,[3,None,None],[2,[4,None,None],None]]

def check_mirror(a,b):
	if a==None and b==None: return True
	if a==None or b==None:  return False
	return a[0]==b[0] and check_mirror(a[1],b[2]) and check_mirror(a[2],b[1])

print check_mirror(a,b)
print check_mirror(a,a)
