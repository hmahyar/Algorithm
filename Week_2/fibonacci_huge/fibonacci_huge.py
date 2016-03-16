# Uses python3
import sys
from math import sqrt


def get_fibonaccihuge(n, m):
    return (n%(2**m))%m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))

