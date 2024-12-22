class Day2:
    """Class for Day2
    """
    levels: list[list[int]] = []
    with open('input', 'r') as file:
        for line in file:
            levels.append([int(num) for num in line.split()])

    def sign(self, x):
        return (x > 0) - (x < 0)

    def is_safe(self, level: list[int]) -> bool:
        size = len(level)

        direction = self.sign(level[1] - level[0])

        for i in range(1, size):
            diff = level[i] - level[i-1]

            if direction != self.sign(diff):
                return False
            if not (1 <= abs(diff) <= 3):
                return False

        return True

    def is_safe2(self, level: list[int]) -> bool:
        size = len(level)

        num_sign_changes = 0
        direction = self.sign(level[1] - level[0])

        for i in range(1, size):
            diff = level[i] - level[i-1]

            if direction != self.sign(diff):
                if num_sign_changes >= 2:
                    return False
                num_sign_changes += 1

            if not (1 <= abs(diff) <= 3):
                return False

        return True

    def part1(self):
        num_safe = 0

        for level in self.levels:
            num_safe += 1 if self.is_safe(level) else 0

        print(num_safe)




if __name__ == "__main__":
    day = Day2()
    day.part1()
