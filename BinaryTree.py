import Queue as Queue 
class BinaryTree(object):
    def __init__(self,rootnode):
        self.tree=[rootnode,[],[],0]

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
            tree.extend([node,[],[],0])
            return True
        elif tree[0]>node: 
            d = self.insert(node,tree[1])
            if d: tree[3]+=1
            if tree[3]==0: return False
            
            else: return True
            
        elif tree[0]<node:
            d = self.insert(node,tree[2])
            if d : tree[3]-=1
            if tree[3]==0: return False
            else: return True

    def remove(self,node,tree):
        self.tree = self._remove(node,tree)
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
    
    def rotation_left(self,rotation_node,tree):
        if tree[0]>rotation_node:
            tree[1] = self.rotation_left(rotation_node,tree[1])
            return tree
        if tree[0]<rotation_node:
            tree[2] = self.rotation_left(rotation_node,tree[2])
            return tree
        else:
            new_root = tree[2]
            tree[2] = new_root[1] 
            new_root[1] = tree
            return new_root 

    def rotation_right(self,rotation_node,tree):
        if tree[0]>rotation_node:
            tree[1] = self.rotation_left(rotation_node,tree[1])
            return tree
        if tree[0]<rotation_node:
            tree[2] = self.rotation_left(rotation_node,tree[2])
            return tree
        else:
            new_root = tree[1]
            tree[1] = new_root[2] 
            new_root[2] = tree
            return new_root

    def serilize(self,tree):
        def serilizer(node):
            if node==[]:
                result.append('*')
            else:
                result.append(str(node[0]))
                serilizer(node[1])
                serilizer(node[2])


        result = []
        serilizer(tree)
        return ' '.join(result)
    def deserilize(self,data):
        def deserilizer():
            val = next(vals)
            if val =='*':
                return []
            else:
                node = [int(val),[],[]]
                node[1] = deserilizer()
                node[2] = deserilizer()
                return node

        
        vals = iter(data.split(' '))
        return deserilizer()        
        
T = BinaryTree(3)
#for i in [3,6,4,9,7,8,2,1,10,9.5,5.5]:
for i in [4,2,1]:
    T.insert(i,T.tree)
print T.serilize(T.tree)
print T.deserilize(T.serilize(T.tree))
#print T.sort(T.tree)
#print 'Max: ',T.max(T.tree)
#print 'Min: ',T.min(T.tree)
#print 'IN Order : ', T.in_order(T.tree)
#print 'Post Order : ', T.post_order(T.tree)
#print 'Pre Order : ', T.pre_order(T.tree)
#print 'Breadth_first_search: ', T.Breadth_first_search(T.tree)
#print 'Distance:',T.distance(T.tree,4,7)
#print T.in_order(T.tree)
#T.remove(9,T.tree)
#print T.in_order(T.tree)
#print T.rotation_left(9,T.tree)
#print T.rotation_right(5,T.tree)


