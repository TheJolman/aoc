import os
import re
from days.base import Day


class Day4(Day):
    """Find 'XMAS' in a word search. It can be horizontal, vertical, diagonal,
    or written backwards."""
    day_num = 4

    file_path = os.path.join(os.path.dirname(__file__), "input")
    file_lines: list[str]
    with open(file_path, "r") as file:
        file_lines = file.readlines()

    def __init__(self):
        self.part1_matches = 0

    def _check_xmas_pattern(self, char: str, matching: int, b_matching: int) -> tuple[int, int]:
        match char:
            case 'X':
                matching = 1 if matching == 0 else 0
                if b_matching == 3:
                    self.part1_matches += 1
                b_matching = 0
            case 'M':
                matching = 2 if matching == 1 else 0
                b_matching = 3 if b_matching == 2 else 0
            case 'A':
                matching = 3 if matching == 2 else 0
                b_matching = 2 if b_matching == 1 else 0
            case 'S':
                if matching == 3:
                    self.part1_matches += 1
                matching = 0
                b_matching = 1 if b_matching == 0 else 0
            case _:
                matching = 0
                b_matching = 0

        return matching, b_matching


    def part1(self) -> int:

        num_rows = len(self.file_lines)
        num_cols = len(self.file_lines[0])

        # horizontal search
        matching = 0
        b_matching = 0
        for row in range(num_rows):
            for col in range(num_cols):
                char = self.file_lines[row][col]
                matching, b_matching = self._check_xmas_pattern(char, matching, b_matching)

        print(f"Matches so far: {self.part1_matches}")

        # vertical search
        matching = 0
        b_matching = 0
        for col in range(num_cols):
            for row in range(num_rows):
                char = self.file_lines[row][col]
                matching, b_matching = self._check_xmas_pattern(char, matching, b_matching)

        print(f"Matches so far: {self.part1_matches}")

        # diagonal search like \
        # start at rightmost column and move left
        matching = 0
        b_matching = 0
        for start_col in range(num_cols-1, -1, -1):
            col = start_col
            row = 0
            while col < num_cols and row < num_rows:
                char = self.file_lines[row][col]
                matching, b_matching = self._check_xmas_pattern(char, matching, b_matching)
                col += 1
                row += 1

        print(f"Matches so far: {self.part1_matches}")

        # Diagonal search like /
        # Start at leftmost column and move right
        matching = 0
        b_matching = 0
        for start_col in range(num_cols):
            col = start_col
            row = 0
            while col >= 0 and row < num_rows:
                char = self.file_lines[row][col]
                matching, b_matching = self._check_xmas_pattern(char, matching, b_matching)
                col -= 1
                row += 1

        print(f"Matches so far: {self.part1_matches}")

        return self.part1_matches


    def part2(self) -> int:
        return 0


if __name__ == "__main__":
    day = Day4()
