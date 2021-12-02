import sys

from aoc.utils.puzzle_input import get_puzzle_input


def main() -> int:
    puzzle_input = get_puzzle_input()

    horizontal, depth, aim, depth2 = 0, 0, 0, 0
    for line in puzzle_input:
        direction, value = line.split(' ')
        if direction == "forward":
            horizontal += int(value)
            depth2 += int(value) * aim
        elif direction == "down":
            depth += int(value)
            aim += int(value)
        elif direction == "up":
            depth -= int(value)
            aim -= int(value)

    print(f"Part 1: {horizontal * depth}")
    print(f"Part 2: {horizontal * depth2}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
