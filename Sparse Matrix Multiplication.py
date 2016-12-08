class Solution(object):
    def multiply(self, A, B):
    	result = [[0 for _ in xrange(len(B[0]))] for __ in xrange(len(A))]
    	for i in xrange(len(A)):
    		for k in xrange(len(A[0])):
    			if A[i][k]:
    				for j in xrange(len(B[0])):
    					result[i][j] += A[i][j]*B[j][k]


    	return result

if __name__ == "__main__":
	A = [[ 1, 0, 0],[-1, 0, 3]]
	B = [[ 7, 0, 0 ],[ 0, 0, 0 ],[ 0, 0, 1 ]]
	print Solution().multiply(A,B)
