from __future__ import annotations
import sys
from collections import defaultdict, namedtuple
from typing import List, NamedTuple, Tuple

from aoc.utils.puzzle_input import get_puzzle_input


class Grid:
    def __init__(self):
        self._grid = defaultdict(int)

    @property
    def overlapping(self) -> int:
        return len([k for k in self._grid.values() if k > 1])

    def add_line(self, a: Point, b: Point, diagonals: bool = False):
        if a.x == b.x:
            for y in range(min(a.y, b.y), max(a.y, b.y) + 1):
                self._grid[Point(a.x, y)] += 1
        if a.y == b.y:
            for x in range(min(a.x, b.x), max(a.x, b.x) + 1):
                self._grid[Point(x, a.y)] += 1
        if diagonals and abs(a.x - b.x) == abs(a.y - b.y):
            if b.x - a.x > 0 and b.y - a.y > 0:
                for n in range(b.x - a.x + 1):
                    self._grid[a.x + n, a.y + n] += 1
            if b.x - a.x > 0 and b.y - a.y < 0:
                for n in range(b.x - a.x + 1):
                    self._grid[a.x + n, a.y - n] += 1
            if b.x - a.x < 0 and b.y - a.y > 0:
                for n in range(a.x - b.x + 1):
                    self._grid[a.x - n, a.y + n] += 1
            if b.x - a.x < 0 and b.y - a.y < 0:
                for n in range(a.x - b.x + 1):
                    self._grid[a.x - n, a.y - n] += 1


class Point(NamedTuple):
    x: int
    y: int

    @staticmethod
    def from_string(s: str) -> Point:
        return Point(int(s.split(',')[0]), int(s.split(',')[1]))


def main() -> int:
    puzzle_input = get_puzzle_input()

    grid_1 = Grid()
    grid_2 = Grid()

    for a, b in get_lines(puzzle_input):
        grid_1.add_line(a, b)
        grid_2.add_line(a, b, diagonals=True)

    print(f"Part 1: {grid_1.overlapping}")
    print(f"Part 2: {grid_2.overlapping}")

    return 0


def get_lines(data: List[str]) -> List[Tuple[Point, Point]]:
    lines = []
    for line in data:
        point_a, point_b = line.split(' -> ')
        lines.append((Point.from_string(point_a), Point.from_string(point_b)))
    return lines


if __name__ == "__main__":
    sys.exit(main())
