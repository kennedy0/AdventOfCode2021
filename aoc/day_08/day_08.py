import sys
from typing import List

from aoc.utils.puzzle_input import get_puzzle_input


class Rules:
    def __init__(self, patterns: List[str]):
        self._rules = dict()
        self._calculate_rules(patterns)

    def _calculate_rules(self, patterns: List[str]):
        # 1, 4, 7, 8
        for p in patterns:
            if len(p) == 2:
                self._rules[p] = 1
            if len(p) == 4:
                self._rules[p] = 4
            if len(p) == 3:
                self._rules[p] = 7
            if len(p) == 7:
                self._rules[p] = 8

        for segment in self.get_segments(7):
            if segment not in self.get_segments(1):
                top_segment = segment

        # 6
        for p in patterns:
            if len(p) == 6:
                for segment in self.get_segments(1):
                    if segment not in p:
                        self._rules[p] = 6
                        top_right_segment = segment

        for segment in self.get_segments(1):
            if segment != top_right_segment:
                bottom_right_segment = segment

        # 2, 5
        for p in patterns:
            if len(p) == 5:
                if bottom_right_segment not in p:
                    self._rules[p] = 2
                if top_right_segment not in p:
                    self._rules[p] = 5

        # 3
        for p in patterns:
            if len(p) == 5:
                if p not in self._rules.keys():
                    self._rules[p] = 3

        # 0
        for p in patterns:
            if len(p) == 6:
                if p not in self._rules.keys():
                    for segment in self.get_segments(3):
                        if segment not in p:
                            self._rules[p] = 0

        # 9
        for p in patterns:
            if p not in self._rules.keys():
                self._rules[p] = 9

    def get_number(self, segments: str) -> int:
        return self._rules.get(segments)

    def get_segments(self, number: int) -> str:
        for k, v in self._rules.items():
            if v == number:
                return k


def main() -> int:
    puzzle_input = get_puzzle_input()

    easy_digits = 0
    output_sum = 0
    for line in puzzle_input:
        patterns, outputs = line.split(' | ')
        patterns = [''.join(sorted(p)) for p in patterns.split(" ")]
        outputs = [''.join(sorted(o)) for o in outputs.split(" ")]
        rules = Rules(patterns)

        digits = []
        for segments in outputs:
            digit = rules.get_number(segments)
            digits.append(digit)
            if digit in (1, 4, 7, 8):
                easy_digits += 1
        output_sum += (digits[0] * 1000) + (digits[1] * 100) + (digits[2] * 10) + digits[3]

    print(f"Part 1: {easy_digits}")
    print(f"Part 2: {output_sum}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
