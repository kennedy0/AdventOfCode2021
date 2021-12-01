import sys

from aoc.utils.puzzle_input import get_puzzle_input


def main() -> int:
    puzzle_input = [int(i) for i in get_puzzle_input()]

    # Part 1
    increases = 0
    for n in range(1, len(puzzle_input)):
        previous_depth = puzzle_input[n-1]
        current_depth = puzzle_input[n]
        if current_depth > previous_depth:
            increases += 1
    print(f"Part 1: {increases}")

    # Part 2
    increases = 0
    for n in range(3, len(puzzle_input)):
        previous_window = (puzzle_input[n-1], puzzle_input[n-2], puzzle_input[n-3])
        current_window = (puzzle_input[n], puzzle_input[n-1], puzzle_input[n-2])
        previous_window_average = sum(previous_window) / len(previous_window)
        current_window_average = sum(current_window) / len(current_window)
        if current_window_average > previous_window_average:
            increases += 1
    print(f"Part 2: {increases}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
