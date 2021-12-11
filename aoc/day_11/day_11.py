import sys
from typing import Generator, List, Tuple

from aoc.utils.puzzle_input import get_puzzle_input


class Grid:
    def __init__(self, puzzle_input: List[str]):
        self.cells = dict()
        self.height = len(puzzle_input)
        self.width = len(puzzle_input[0])
        self.flashes = 0

        self._init_map(puzzle_input)

    def _init_map(self, puzzle_input: List[str]):
        for y, row in enumerate(puzzle_input):
            for x, point in enumerate(row):
                self.cells[(x, y)] = int(point)

    @property
    def all_flashed(self) -> bool:
        if sum(self.cells.values()) == 0:
            return True
        return False

    @property
    def iter_cells(self) -> Generator[Tuple[int, int], None, None]:
        for y in range(self.height):
            for x in range(self.width):
                yield x, y

    def get_value(self, x: int, y: int) -> int:
        return self.cells.get((x, y))

    def reset_value(self, x: int, y: int):
        self.cells[(x, y)] = 0

    def increase_value(self, x: int, y: int):
        value = self.get_value(x, y) + 1
        self.cells[(x, y)] = value
        if value == 10:
            self.flash(x, y)

    def flash(self, x: int, y: int):
        self.flashes += 1
        for nx, ny in self.get_neighbor_coordinates(x, y):
            self.increase_value(nx, ny)

    def get_neighbor_coordinates(self, x: int, y: int) -> List[Tuple[int, int]]:
        coordinates = []
        for yy in [y-1, y, y+1]:
            for xx in [x-1, x, x+1]:
                if xx == x and yy == y:
                    continue
                if xx in range(self.width) and yy in range(self.height):
                    coordinates.append((xx, yy))
        return coordinates


def main() -> int:
    puzzle_input = get_puzzle_input()
    grid = Grid(puzzle_input)

    step = 0
    flashes = 0
    all_flashed = 0
    while True:
        step += 1
        for x, y in grid.iter_cells:
            grid.increase_value(x, y)
        for x, y in grid.iter_cells:
            if grid.get_value(x, y) > 9:
                grid.reset_value(x, y)

        if step == 100:
            flashes = grid.flashes
        if grid.all_flashed:
            all_flashed = step
            break

    print(f"Part 1: {flashes}")
    print(f"Part 2: {all_flashed}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
