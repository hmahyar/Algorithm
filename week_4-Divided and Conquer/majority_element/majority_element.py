# Uses python3
import sys

def get_majority_element(a, left, right):
    print (a[left:right],left,right,a[left])
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    
    k = n//2
    elem_left  = get_majority_element(a, left, left+k-1)
    elem_right = get_majority_element(a, left+k, right)
    print ('L:',elem_left,'R:',elem_right)
    if elem_left==elem_right:
        return elem_left

    return -1

if __name__ == '__main__':
    #input = sys.stdin.read()
    n, *a = 5,1,1,0,4,1#list(map(int, input.split()))
    
    get_majority_element(a, 0, n)

    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
