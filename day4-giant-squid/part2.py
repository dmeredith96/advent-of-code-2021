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
                if int(current_node.number) == num_to_mark:
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
    last_winning_num_called = 0
    last_winning_board_sum = 0
    current_num = 0
    solved_boards = []
    for i in range(5):
        current_num = numbers_to_draw.pop(0)
        for board in bingo_boards:
            board.mark_values(current_num)
    while (len(numbers_to_draw) > 0):
        print (numbers_to_draw)
        for board in bingo_boards:
            if board.is_solved():
                solved_boards.append(board)
                bingo_boards.remove(board)
                last_winning_board_sum = board.sum_of_unmarked_numbers()
                last_winning_num_called = current_num
        current_num = numbers_to_draw.pop(0)
        for board in bingo_boards:
            board.mark_values(current_num)
    print (last_winning_board_sum, last_winning_num_called)
    return last_winning_board_sum * last_winning_num_called


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