from typing import List
from fractions import Fraction

class Line():
    def __init__(self, x1: int, x2: int, y1: int, y2: int) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

class Grid():
    def __init__(self, max_x: int, max_y: int) -> None:
        self.max_x = max_x
        self.max_y = max_y
        self.grid = []
        for i in range(max_y+1):
            row = []
            for j in range(max_x+1):
                row.append(0)
            self.grid.append(row)

    def update_grid(self, line: Line) -> None:
        if (line.x1 == line.x2):
            for i in range(min(line.y1, line.y2), max(line.y1, line.y2)+1):     
                self.grid[i][line.x1] += 1
        elif (line.y1 == line.y2):
            for i in range(min(line.x1, line.x2), max(line.x1, line.x2)+1):
                self.grid[line.y1][i] += 1
        else:
            slope = Fraction(line.y2 - line.y1, line.x2 - line.x1)
            y1 = line.y1
            y2 = line.y2
            x1 = line.x1
            x2 = line.x2
            if (slope == -1):
                if (x1 <= x2):
                    while (x1 <= x2):
                        self.grid[y1][x1] += 1
                        x1 += 1
                        y1 -= 1
                else:
                    while (x2 <= x1):
                        self.grid[y2][x2] += 1
                        x2 += 1
                        y2 -= 1
            else:
                if (x1 <= x2):
                    while (x1 <= x2):
                        self.grid[y1][x1] += 1
                        x1 += 1
                        y1 += 1
                else:
                    while (x2 <= x1):
                        self.grid[y2][x2] += 1
                        x2 += 1
                        y2 += 1
    
    def get_total_overlapping_points(self) -> int:
        total = 0
        for row in self.grid:
            for column in row:
                if column > 1:
                    total += 1
        return total


def solve():
    all_lines = get_line_objects()
    max_x = 0
    max_y = 0
    for line in all_lines:
        if line.x1 > max_x or line.x2 > max_x:
            max_x = max(line.x1, line.x2)
        if line.y1 > max_y or line.y2 > max_y:
            max_y = max(line.y1, line.y2)
    grid = Grid(max_x, max_y)
    for line in all_lines:
        grid.update_grid(line)
    print(grid.get_total_overlapping_points())

def get_line_objects():
    all_lines: List[Line] = []
    with open('input.txt') as file:
        for line in file:
            raw_line_list = ([x.strip() for x in line.split('->')])
            for i,k in zip(raw_line_list[0::2], raw_line_list[1::2]):
                x1y1 = i.split(',')
                x2y2 = k.split(',')
                all_lines.append(Line(int(x1y1[0]), int(x2y2[0]), int(x1y1[1]), int(x2y2[1])))
    return all_lines
                

solve()