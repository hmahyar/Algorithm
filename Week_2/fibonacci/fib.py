# Uses python3
from math import sqrt
def calc_fib(n):
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

n = int(input())
print (calc_fib(n))

