import Queue as Queue 
class BinaryTree(object):
    def __init__(self,rootnode):
        self.tree=[rootnode,[],[]]

    def in_order(self,tree):
        if tree:
            if tree[1]:
                self.in_order(tree[1])
            print tree[0],
            if tree[2]:
                self.in_order(tree[2])

    def post_order(self,tree):
        if tree:
            if tree[1]:
                self.post_order(tree[1])
            if tree[2]:
                self.post_order(tree[2])
            print tree[0],

    def pre_order(self,tree):
        if tree:
            print tree[0],
            if tree[1]:
                self.pre_order(tree[1])
            if tree[2]:
                self.pre_order(tree[2])
    
    def Breadth_first_search(self,tree):
        Q = Queue.Queue()
        Q.put(tree)
        while not Q.empty():
            node =Q.get() 
            print node[0],
            if(node[1]):
                Q.put(node[1])
            if(node[2]):
                Q.put(node[2])
            
    def insert(self,node,tree):
        if len(tree)==0:
            tree.append(node)
            tree.append([])
            tree.append([])

        if tree[0]==node:
            return 'Already Exists'
        elif tree[0]>node: 
            self.insert(node,tree[1])
        else:
            self.insert(node,tree[2])

    def remove(self,node , tree):
        self.tree=  self._remove(node,tree)
    def _remove(self,key,tree):
        if tree == []:
            return tree
        elif tree[0]>key:
            tree[1] =self._remove(key,tree[1])
            return tree
        elif tree[0]<key:
            tree[2] =self._remove(key,tree[2])
            return tree
        else:
            if tree[1]==[]:
                return tree[2]
            elif tree[2]==[]:
                return tree[1]
            else:
                replacement = self.min(tree[2])
                tree[0] = replacement
                self._remove(replacement,tree[2])
                return tree 
    def max(self,tree):
        if tree[2]:
            return self.max(tree[2])
        else:
            return tree[0] 
    
    def min(self,tree):
        if tree[1]:
            return self.min(tree[1])
        else:
            return tree[0] 
    def search(self,tree,key,path):
        if tree!=[]:
            path.append(tree[0])
            if tree[0]==key:   
                return path
            elif tree[0]>key:  
                return self.search(tree[1],key,path)
            else:
                return self.search(tree[2],key,path)
        return[]
        #raise Exception('Not Found')
    def distance(self,tree,a,b):
        Z = self.search(tree,a,[])
        Y = self.search(tree,b,[])
        print len(set(Y)^set(Z))

T = BinaryTree(5)
for i in [3,6,4,9,7,8,2,1,10,9.5,5.5]:
#for i in [5,7,2,4]:
    T.insert(i,T.tree)
#print T.sort(T.tree)
#print 'Max: ',T.max(T.tree)
#print 'Min: ',T.min(T.tree)
#print 'IN Order : ', T.in_order(T.tree)
#print 'Post Order : ', T.post_order(T.tree)
#print 'Pre Order : ', T.pre_order(T.tree)
#print 'Breadth_first_search: ', T.Breadth_first_search(T.tree)
#print 'Distance:',T.distance(T.tree,4,7)
print T.in_order(T.tree)
T.remove(9,T.tree)
print T.in_order(T.tree)


