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

    def _check_line(self, line: str) -> int:
        count = 0
        for i in range(len(line) - 3):
            if line[i:i+4] == 'XMAS':
                count += 1
            if line[i:i+4] == 'SAMX':
                count += 1
        return count


    def part1(self) -> int:
        grid = [line.strip() for line in self.file_lines]

        total = 0
        rows = len(grid)
        cols = len(grid[0])

        # Horizontal
        for row in grid:
            total += self._check_line(row)

        # Vertical
        for col in range(cols):
            vertical = ''.join(grid[row][col] for row in range(rows))
            total += self._check_line(vertical)

        # Diagonal \
        for row_start in range(rows):
            for col_start in range(cols):
                diagonal = ''
                r, c = row_start, col_start
                while r < rows and c < cols:
                    diagonal += grid[r][c]
                    r += 1
                    c += 1
                total += self._check_line(diagonal)

        # Diagonal /
        for row_start in range(rows):
            for col_start in range(cols):
                diagonal = ''
                r, c = row_start, col_start
                while r < rows and c >= 0:
                    diagonal += grid[r][c]
                    r += 1
                    c -= 1
                total += self._check_line(diagonal)

        return total


    def part2(self) -> int:
        return 0


if __name__ == "__main__":
    day = Day4()
