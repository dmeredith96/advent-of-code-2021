from statistics import *
from numpy import *

def solve():
    x = fromfile(open('input.txt'), int, sep=',')
    print(sum(abs(x - median(x))))

print(solve()) 