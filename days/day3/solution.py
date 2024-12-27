import os
from days.base import Day

class Day3(Day):
    day_num = 3

    file_path = os.path.join(os.path.dirname(__file__), 'input')
    file_buffer = ""
    with open(file_path, 'r') as file:
        file_buffer = file.read()


if __name__ == "__main__":
    day = Day3()
    print(day.file_buffer)

