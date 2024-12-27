import os
from days.base import Day

class Day1(Day):
    day_num = 1

    left: list[int] = []
    right: list[int] = []

    file_path = os.path.join(os.path.dirname(__file__), 'input')
    with open(file_path, 'r') as file:
        for line in file:
            cols = line.split()
            left.append(int(cols[0]))
            right.append(int(cols[1]))

    def part1(self) -> int:
        self.left.sort()
        self.right.sort()
        self.right.sort()

        diffs = [abs(lval - rval) for lval, rval in zip(self.left, self.right)]

        # print(sum(diffs))
        return sum(diffs)

    def part2(self) -> int:
        counts = {lval: self.right.count(lval) for lval, rval in zip(self.left, self.right)}

        similarities = [lval * counts[lval] for lval, rval in zip(self.left, self.right)]

        # print(sum(similarities))
        return sum(similarities)
