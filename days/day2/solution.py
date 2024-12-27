import os
from utils.helpers import sign
from days.base import Day

class Day2(Day):
    """Class for Day2"""

    day_num = 2

    levels: list[list[int]] = []
    file_path = os.path.join(os.path.dirname(__file__), 'input')
    with open(file_path, "r") as file:
        for line in file:
            levels.append([int(num) for num in line.split()])


    def _is_safe(self, level: list[int]) -> bool:
        size = len(level)

        direction = sign(level[1] - level[0])

        for i in range(1, size):
            diff = level[i] - level[i - 1]

            if direction != sign(diff):
                return False
            if not (1 <= abs(diff) <= 3):
                return False

        return True

    def _is_safe2(self, level: list[int]) -> bool:
        if self._is_safe(level):
            return True

        size = len(level)

        for i in range(size):
            test_level = level[:i] + level[i + 1 :]
            if self._is_safe(test_level):
                return True

        return False

    def part1(self) -> int:
        num_safe = 0

        for level in self.levels:
            num_safe += 1 if self._is_safe(level) else 0

        # print(num_safe)
        return num_safe

    def part2(self) -> int:
        num_safe = 0

        for level in self.levels:
            num_safe += 1 if self._is_safe2(level) else 0

        # print(num_safe)
        return num_safe


if __name__ == "__main__":
    day = Day2()
    day.part1()
    day.part2()
