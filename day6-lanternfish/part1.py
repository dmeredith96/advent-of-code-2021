from typing import List


class Lanternfish():
    DAYS_TO_RESET_TO = 6
    def __init__(self, days_remaining: int = 8) -> None:
        self.days_remaining = days_remaining

    def reset_days_remaining(self):
        self.days_remaining = self.DAYS_TO_RESET_TO

def solve():
    current_day = 1
    days_to_run = 80
    all_lanternfish = create_initial_lanernfish()
    while (current_day <= days_to_run):
        lanternfish_to_add = []
        for lanternfish in all_lanternfish:
            if (lanternfish.days_remaining == 0):
                lanternfish_to_add.append(Lanternfish())
                lanternfish.reset_days_remaining()
            else:
                lanternfish.days_remaining -= 1
        for lanternfish in lanternfish_to_add:
            all_lanternfish.append(lanternfish)
        current_day += 1
    print(len(all_lanternfish))

def create_initial_lanernfish():
    all_lanternfish: List[Lanternfish] = []
    with open('input.txt') as file:
        split_input = file.read().split(',')
        for entry in split_input:
            all_lanternfish.append(Lanternfish(int(entry)))
    return all_lanternfish

print(solve())