# Unique Binary Search Trees 
# G(0) = 1
# G(1) = 1
# G(2) = G(0)*G(1) + G(1)*G(0) = 2
# G(3) = G(0)*G(2) + G(1)*G(1) + G(2)*G(0) =  5
# G(n)=  G(1)*G(n-1) + G(2)*G(n-2) + G(3)*G(n-3) = 

#i => 2 to n
	#j => 1 to i
		#G(i)+= G(i-j)*G(j-1)

def numTrees(n):
    G = [0 for _ in range(n+1)]
    G[0] =1
    G[1] =1
    print 0,0,0,G
    for i in xrange(2,n+1):
        for j in xrange(1,i+1):
            G[i] += G[i-j]*G[j-1] 
    
    return G[-1]

print numTrees(3)