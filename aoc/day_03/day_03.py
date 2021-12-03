import sys
from copy import copy
from decimal import localcontext, Decimal, ROUND_HALF_UP
from enum import Enum
from typing import List

from aoc.utils.puzzle_input import get_puzzle_input


class BitCriteriaMode(Enum):
    BIT_CRITERIA_MOST_COMMON = 0
    BIT_CRITERIA_LEAST_COMMON = 1


def main() -> int:
    puzzle_input = get_puzzle_input()
    puzzle_input = [[int(r) for r in row] for row in puzzle_input]

    # Part 1
    gamma_bits = most_common_bits(puzzle_input)
    epsilon_bits = invert_bits(gamma_bits)
    gamma = bits_to_binary(gamma_bits)
    epsilon = bits_to_binary(epsilon_bits)
    print(f"Part 1: {gamma * epsilon}")

    # Part 2
    o2_rating = bit_criteria_filter(puzzle_input, BitCriteriaMode.BIT_CRITERIA_MOST_COMMON)
    co2_rating = bit_criteria_filter(puzzle_input, BitCriteriaMode.BIT_CRITERIA_LEAST_COMMON)
    print(f"Part 2: {o2_rating * co2_rating}")

    return 0


def most_common_bits(binary_numbers: List[List[int]]) -> List[int]:
    columns = len(binary_numbers[0])
    rows = len(binary_numbers)
    bit_sum = [0] * columns

    for line in binary_numbers:
        for i in range(columns):
            bit_sum[i] += line[i]

    bit_average = [(b / rows) for b in bit_sum]

    mcb = []
    with localcontext() as ctx:
        ctx.rounding = ROUND_HALF_UP
        for b in bit_average:
            mcb.append(int(Decimal(b).to_integral_value()))
    return mcb


def invert_bits(bits: List[int]) -> List[int]:
    return [0 if r == 1 else 1 for r in bits]


def bits_to_binary(bits: List[int]) -> int:
    return int("".join([str(b) for b in bits]), 2)


def bit_criteria_filter(binary_numbers: List[List[int]], mode: BitCriteriaMode) -> int:
    data = copy(binary_numbers)
    column = 0
    while True:
        if mode == BitCriteriaMode.BIT_CRITERIA_MOST_COMMON:
            bit_criteria = most_common_bits(data)[column]
        else:
            bit_criteria = invert_bits(most_common_bits(data))[column]
        data = [row for row in data if row[column] == bit_criteria]
        if len(data) == 1:
            return bits_to_binary(data[0])
        else:
            column += 1


if __name__ == "__main__":
    sys.exit(main())
