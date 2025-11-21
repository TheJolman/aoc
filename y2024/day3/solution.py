import os
import re
from typing import Any


class Day3:
    file_path = os.path.join(os.path.dirname(__file__), "input")
    file_buffer: str
    with open(file_path, "r") as file:
        file_buffer = file.read()

    mul_pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    number_pattern = re.compile(r"\d{1,3}")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")

    def _mul(self, mul_statement: str) -> int:
        n1, n2 = map(int, self.number_pattern.findall(mul_statement))
        return n1 * n2

    def part1(self) -> int:
        matches = self.mul_pattern.findall(self.file_buffer)
        return sum(self._mul(match) for match in matches)

    def part2(self) -> int:
        patterns = [self.mul_pattern, self.do_pattern, self.dont_pattern]

        all_matches: list[dict[str, Any]] = []

        for pattern_idx, pattern in enumerate(patterns):
            for match in re.finditer(pattern, self.file_buffer):
                all_matches.append(
                    {
                        "start": match.start(),
                        "match": match.group(),
                        "pattern_idx": pattern_idx,
                    }
                )

        all_matches = sorted(all_matches, key=lambda x: x["start"])

        do = True
        sum = 0
        for match_dict in all_matches:
            if match_dict["pattern_idx"] == 2:
                do = False
            elif match_dict["pattern_idx"] == 1:
                do = True
            elif match_dict["pattern_idx"] == 0 and do:
                sum += self._mul(match_dict["match"])

        return sum
