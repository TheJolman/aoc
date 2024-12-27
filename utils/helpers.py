from typing import Union
from days.base import Day

def sign(x: Union[int, float]):
    """Returns 1 for a positive number, and -1 for a negative number."""
    return (x > 0) - (x < 0)

def print_parts(day: Day):
    print(f"Day {day.day_num}: {day.part1():<10} {day.part2():<10}")
