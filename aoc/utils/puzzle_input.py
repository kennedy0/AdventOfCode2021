from pathlib import Path
from typing import List


def get_puzzle_input() -> List[str]:
    input_file = Path.cwd() / "input.txt"
    with open(input_file, 'r') as fp:
        puzzle_input = [line.strip() for line in fp.readlines()]
    return puzzle_input
