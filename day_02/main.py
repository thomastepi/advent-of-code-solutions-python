from utils import read_file_by_line
from typing import List


def part1(data: List[str]) -> int:
    p1_value = {
        'A X': 1 + 3,
        'A Y': 2 + 6,
        'A Z': 3 + 0,
        'B X': 1 + 0,
        'B Y': 2 + 3,
        'B Z': 3 + 6,
        'C X': 1 + 6,
        'C Y': 2 + 0,
        'C Z': 3 + 3,
    }
    out = 0
    for line in data:
        out += p1_value[line]
    return out

def part2(data: List[str]) -> int:
    p2_value = {
        'A X': 3 + 0,
        'A Y': 1 + 3,
        'A Z': 2 + 6,
        'B X': 1 + 0,
        'B Y': 2 + 3,
        'B Z': 3 + 6,
        'C X': 2 + 0,
        'C Y': 3 + 3,
        'C Z': 1 + 6,
    }
    out = 0
    for line in data:
        out += p2_value[line]
    return out


def main():
    data = read_file_by_line('input.txt')
    print(f'part 1: {part1(data)}')
    print(f'part 2: {part2(data)}')


if __name__ == '__main__':
    main()
