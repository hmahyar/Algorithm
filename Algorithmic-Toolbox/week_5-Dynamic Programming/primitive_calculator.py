# Uses python3
import sys

def optimal_sequence(n,memo,sequence):
    print (memo,'--',n)
    input('\n')
    sequence.append(n)
    if n==1:
        return 1
    
    if n in memo:
        print ('Reading From Memo')
        return memo[n]

    
    if n % 3 == 0:
        memo[n]=optimal_sequence(n // 3,memo,sequence)
        print ('@3',memo[n])
        #return memo[n]
    
    elif n % 2 == 0:
        memo[n]=optimal_sequence(n // 2,memo,sequence)
        print ('@2',memo[n])
        #return memo[n]
    
    else:
        memo[n]=optimal_sequence(n - 1,memo,sequence)
        print ('@1',memo[n])
        #return memo[n]
    #return reversed(sequence)
    #print (memo)
    print (sequence)
#input = sys.stdin.read()
n = 96234#int(input)
#sequence = list(optimal_sequence(n,{}))
print (optimal_sequence(n,{},[]))
#print(len(sequence) - 1)
#for x in sequence:
#    print(x, end=' ')
