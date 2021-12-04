import sys
from typing import List, Tuple

from aoc.utils.puzzle_input import get_puzzle_input


class BingoBoard:
    def __init__(self, data: List[List[int]]):
        self._board = dict()  # {(x, y): value ...}
        self._positions = dict()  # {value: (x, y), ...}
        self._solved = set()
        self._has_bingo = False
        self._winning_number = 0
        self._init_board(data)

    @property
    def has_bingo(self) -> bool:
        return self._has_bingo

    @property
    def score(self) -> int:
        sum_unmarked = 0
        for position, value in self._board.items():
            if position not in self._solved:
                sum_unmarked += value
        return sum_unmarked * self._winning_number

    def _init_board(self, data: List[List[int]]):
        for y, row in enumerate(data):
            for x, n in enumerate(row):
                self._board[(x, y)] = n
                self._positions[n] = (x, y)

    def call_number(self, number: int):
        position = self.get_position(number)
        if position is None:
            return
        self._solved.add(position)
        self.check_bingo(position)
        if self.has_bingo:
            self._winning_number = number

    def get_position(self, number: int) -> Tuple[int, int]:
        return self._positions.get(number)

    def check_bingo(self, position: Tuple[int, int]):
        x, y = position
        self.check_row(y)
        self.check_column(x)
        # self.check_diagonal_tl_br()
        # self.check_diagonal_tr_bl()

    def check_row(self, row: int):
        for x in range(5):
            if not self.square_solved(x, row):
                return
        self._has_bingo = True

    def check_column(self, column: int):
        for y in range(5):
            if not self.square_solved(column, y):
                return False
        self._has_bingo = True

    def check_diagonal_tl_br(self):
        for x, y in [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]:
            if not self.square_solved(x, y):
                return False
        self._has_bingo = True

    def check_diagonal_tr_bl(self):
        for x, y in [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)]:
            if not self.square_solved(x, y):
                return False
        self._has_bingo = True

    def square_solved(self, column: int, row: int):
        return (column, row) in self._solved


def main() -> int:
    puzzle_input = get_puzzle_input()

    bingo_numbers = [int(p) for p in puzzle_input[0].split(',')]
    boards = generate_boards(puzzle_input[2:])

    solved_boards = []
    for t, n in enumerate(bingo_numbers):
        for i, board in enumerate(boards):
            if board.has_bingo:
                continue
            board.call_number(n)
            if board.has_bingo:
                solved_boards.append(board)

    print(f"Part 1: {solved_boards[0].score}")
    print(f"Part 1: {solved_boards[-1].score}")
    return 0


def generate_boards(data: List[str]) -> List[BingoBoard]:
    boards = []
    rows = []
    for line in data:
        if line == "":
            boards.append(BingoBoard(rows))
            rows = []
            continue
        rows.append([int(l) for l in line.replace('  ', ' ').split(' ')])  # noqa
    boards.append(BingoBoard(rows))
    return boards


if __name__ == "__main__":
    sys.exit(main())
