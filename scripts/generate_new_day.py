import shutil
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent
TEMPLATE_FILE = PROJECT_ROOT / "resources" / "template.py"
AOC_DIR = PROJECT_ROOT / "aoc"


def main():
    new_folder = create_folder()
    copy_template_file(new_folder)
    create_input_file(new_folder)


def create_folder() -> Path:
    day = 1
    new_folder_path = AOC_DIR / folder_name(day)
    while new_folder_path.exists():
        day += 1
        new_folder_path = AOC_DIR / folder_name(day)
    new_folder_path.mkdir()
    return new_folder_path


def folder_name(day: int) -> str:
    return f"day_{day:02d}"


def copy_template_file(path: Path):
    file_name = f"{path.name}.py"
    shutil.copy2(TEMPLATE_FILE, path / file_name)


def create_input_file(path: Path):
    input_file = path / "input.txt"
    input_file.touch()


if __name__ == "__main__":
    sys.exit(main())
