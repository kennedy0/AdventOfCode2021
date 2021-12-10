import sys

from aoc.utils.puzzle_input import get_puzzle_input


def main() -> int:
    puzzle_input = get_puzzle_input()

    illegal_characters = ""
    autocomplete_lines = []
    for line in puzzle_input:
        error = False
        queue = []
        for x in line:
            if x in "([{<":
                queue.append(x)
            else:
                if valid_closer(x, queue[-1]):
                    queue.pop()
                else:
                    error = True
                    illegal_characters += x
                    break
        if error is False:
            autocomplete_lines.append(autocomplete(''.join(queue)))

    autocomplete_scores = [autocomplete_score(i) for i in autocomplete_lines]
    middle_score = sorted(autocomplete_scores)[len(autocomplete_scores)//2]

    print(f"Part 1: {error_score(illegal_characters)}")
    print(f"Part 2: {middle_score}")
    return 0


def valid_closer(char: str, last_in_queue: str) -> bool:
    pair = f"{last_in_queue}{char}"
    if pair in ["()", "[]", "{}", "<>"]:
        return True
    return False


def error_score(characters: str) -> int:
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    return sum(points[c] for c in characters)


def autocomplete(characters: str) -> str:
    return "".join(reversed(characters)).replace('(', ')').replace('[', ']').replace('{', '}').replace('<', '>')


def autocomplete_score(characters: str) -> int:
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    score = 0
    for c in characters:
        score *= 5
        score += points[c]
    return score


if __name__ == "__main__":
    sys.exit(main())
