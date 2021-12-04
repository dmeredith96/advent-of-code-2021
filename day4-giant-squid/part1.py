from typing import List, Tuple


class BingoBoard:
    def __init__(self, nodes) -> None:
        self.nodes = nodes

    def is_solved(self) -> bool:
        for i in range(5):
            if (self.__is_row_solved(i)):
                return True
            elif(self.__is_column_solved(i)):
                return True
        return False

    def sum_of_unmarked_numbers(self) -> int:
        sum = 0
        for node_row in self.nodes:
            for current_node in node_row:
                if current_node.marked is False:
                    sum += current_node.number
        return sum

    def mark_values(self, num_to_mark: int) -> None:
        for node_row in self.nodes:
            for current_node in node_row:
                print(current_node.number, num_to_mark)
                if int(current_node.number) == num_to_mark:
                    print('marking node')
                    current_node.marked = True

    def __is_row_solved(self, rowIndex: int) -> bool:
        return self.nodes[rowIndex][0].marked & self.nodes[rowIndex][1].marked & self.nodes[rowIndex][2].marked & self.nodes[rowIndex][3].marked & self.nodes[rowIndex][4].marked
    def __is_column_solved(self, colIndex: int) -> bool:
        return self.nodes[0][colIndex].marked & self.nodes[1][colIndex].marked & self.nodes[2][colIndex].marked & self.nodes[3][colIndex].marked & self.nodes[4][colIndex].marked


class BingoNode:
    def __init__(self, number):
        self.number: int = number
        self.marked: bool = False

    def mark(self, value: bool):
        self.marked = value

def solve():
    numbers_to_draw, bingo_boards = create_bingo_boards()
    # start off by drawing 5 numbers and marking boards
    current_num = 0
    for i in range(5):
        current_num = numbers_to_draw.pop(0)
        for board in enumerate(bingo_boards):
            board[1].mark_values(current_num)
    while (len(numbers_to_draw) > 0):
        print (numbers_to_draw)
        for board in enumerate(bingo_boards):
            if board[1].is_solved():
                return board[1].sum_of_unmarked_numbers() * current_num
        current_num = numbers_to_draw.pop(0)
        print(current_num)
        for board in enumerate(bingo_boards):
            board[1].mark_values(current_num)


def create_bingo_boards() -> Tuple[list[int], list[BingoBoard]]:
    numbers_to_draw = []
    bingo_boards = []
    current_board: List[BingoBoard] = []
    with open('input.txt') as in_file:
        for line in nonblank_lines(in_file):
            # Get the numbers_to_draw on the first line
            if numbers_to_draw == []:
                numbers_to_draw = [int(x) for x in line.split(",")]
                continue
            current_line: List[BingoNode] = []
            for current_num in line.split():
                current_line.append(BingoNode(int(current_num)))
            current_board.append(current_line)
            # Every 5 lines is a new bingo board
            if (len(current_board) == 5):
                bingo_boards.append(BingoBoard(current_board))
                current_board = []
    return numbers_to_draw, bingo_boards

def nonblank_lines(f):
    for l in f: 
        line = l.rstrip()
        if line:
            yield line

print(solve())