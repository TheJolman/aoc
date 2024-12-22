left: list[int] = []
right: list[int] = []

with open('input', 'r') as file:
    for line in file:
        cols = line.split()
        left.append(int(cols[0]))
        right.append(int(cols[1]))

def part1():
    left.sort()
    right.sort()

    diffs = [abs(lval - rval) for lval, rval in zip(left, right)]

    print(sum(diffs))

def part2():
    counts = {lval: right.count(lval) for lval, rval in zip(left, right)}

    similarities = [lval * counts[lval] for lval, rval in zip(left, right)]

    print(sum(similarities))

part2()
