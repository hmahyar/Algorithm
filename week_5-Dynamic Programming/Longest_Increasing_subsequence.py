def longest_increasing_subsequense(seq):
    M = [1]*len(seq)
    for i in range(1,len(seq)):
        for j in range(i):
            if seq[i]>seq[j]:
                M[i]=max(M[i],M[j]+1)

    ls=[M[-1]]
    result=[]
    for k in range(len(seq)-1,0,-1):
        if M[k]<ls[-1]:
            ls.append(M[k])
            result.append(seq[k])
        elif M[k]>ls[-1] and M[k]>ls[0] :
            ls=[M[k]]
            result=[seq[k]]
    
    return result[-1::-1]
print  longest_increasing_subsequense([3,4,-1,0,6,2,3,2])
