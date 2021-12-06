from typing import List
from collections import deque

ary = deque([0,0,0,0,0,0,0,0,0])
def solve():
    current_day = 1
    days_to_run = 256 
    create_initial_lanternfish_array()
    while (current_day <= days_to_run):
        lanternfish_to_add = ary[0]
        ary.rotate(-1)
        ary[8]=lanternfish_to_add
        ary[6]+=lanternfish_to_add
        current_day +=1
    
    print(sum(ary))

def create_initial_lanternfish_array():
    with open('input.txt') as file:
        split_input = file.read().split(',')
        for entry in split_input:
            int_entry = int(entry)
            ary[int_entry] += 1

print(solve())