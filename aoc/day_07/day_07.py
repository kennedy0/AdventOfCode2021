import sys

from aoc.utils.puzzle_input import get_puzzle_input


def main() -> int:
    puzzle_input = get_puzzle_input()
    positions = [int(p) for p in puzzle_input[0].split(',')]

    positions.sort()
    median = positions[int(len(positions)/2)]
    mean = int(sum(positions) / len(positions))

    # Part 1
    fuel = 0
    for p in positions:
        fuel += abs(p - median)
    print(f"Part 1: {fuel}")

    # Part 2
    fuel = 0
    for p in positions:
        fuel += triangular_number(abs(p - mean))
    print(f"Part 2: {fuel}")

    return 0


def triangular_number(n: int) -> int:
    return int((n * (n + 1)) / 2)


if __name__ == "__main__":
    sys.exit(main())
