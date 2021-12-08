from statistics import *
from numpy import *

def solve():
    x = fromfile(open('input.txt'), int, sep=',')
    fuel = lambda d: d*(d+1)/2
    print(min(sum(fuel(abs(x - floor(mean(x))))),
          sum(fuel(abs(x - ceil(mean(x)))))))

print(solve()) 