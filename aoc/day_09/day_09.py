import math
import sys
from typing import Generator, List, Tuple

from aoc.utils.puzzle_input import get_puzzle_input


class HeightMap:
    def __init__(self, puzzle_input: List[str]):
        self._map = dict()
        self.height = len(puzzle_input)
        self.width = len(puzzle_input[0])

        self._init_map(puzzle_input)

    def _init_map(self, puzzle_input: List[str]):
        for y, row in enumerate(puzzle_input):
            for x, point in enumerate(row):
                self._map[(x, y)] = int(point)

    @property
    def iter_points(self) -> Generator[Tuple[int, int], None, None]:
        for y in range(self.height):
            for x in range(self.width):
                yield x, y

    def get_value(self, x: int, y: int) -> int:
        return self._map.get((x, y))

    @staticmethod
    def get_neighbor_coordinates(x: int, y: int) -> List[Tuple[int, int]]:
        return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    def get_neighbor_values(self, x: int, y: int) -> List[int]:
        neighbors = []
        for xx, yy in self.get_neighbor_coordinates(x, y):
            value = self.get_value(xx, yy)
            if value is not None:
                neighbors.append(value)
        return neighbors

    def is_low_point(self, x: int, y: int) -> bool:
        value = self.get_value(x, y)
        if all(value < n for n in self.get_neighbor_values(x, y)):
            return True
        return False

    def get_basin_size(self, x: int, y: int) -> int:
        visited = []
        to_visit = [(x, y)]
        while len(to_visit):
            for i, j in to_visit[:]:
                to_visit.remove((i, j))
                visited.append((i, j))
                value = self.get_value(i, j)
                for nx, ny in self.get_neighbor_coordinates(i, j):
                    neighbor = self.get_value(nx, ny)
                    if neighbor is not None:
                        if neighbor == 9:
                            continue
                        if neighbor > value and (nx, ny) not in visited and (nx, ny) not in to_visit:
                            to_visit.append((nx, ny))
        return len(visited)


def main() -> int:
    puzzle_input = get_puzzle_input()
    height_map = HeightMap(puzzle_input)

    low_points = []
    basins = []
    for x, y in height_map.iter_points:
        if height_map.is_low_point(x, y):
            value = height_map.get_value(x, y)
            low_points.append(value)
            basins.append(height_map.get_basin_size(x, y))
    risk_level = sum([p+1 for p in low_points])
    largest_basin_sizes = sorted(basins)[-3:]

    print(f"Part 1: {risk_level}")
    print(f"Part 2: {math.prod(largest_basin_sizes)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
