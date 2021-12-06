import sys

from aoc.utils.puzzle_input import get_puzzle_input


def main() -> int:
    puzzle_input = get_puzzle_input()
    fish = [int(p) for p in puzzle_input[0].split(',')]

    print(f"Part 1: {sum([calculate_population(f, 80) for f in fish])}")
    print(f"Part 2: {sum([calculate_population(f, 256) for f in fish])}")

    return 0


def memoize(func):
    cache = dict()

    def memoized_func(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return memoized_func


@memoize
def calculate_population(timer: int, days: int) -> int:
    if days == 0:
        return 1
    if timer == 0:
        return calculate_population(6, days - 1) + calculate_population(8, days - 1)
    else:
        return calculate_population(timer - 1, days - 1)


if __name__ == "__main__":
    sys.exit(main())
