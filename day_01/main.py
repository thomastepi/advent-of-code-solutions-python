from typing import List
from utils import read_file_by_line


def calculate_calorie_list(raw_data: List[str]) -> List[int]:
    out = []
    total = 0
    for line in raw_data:
        if line != '':
            total = total + int(line)
        else:
            out.append(total)
            total = 0
    return out


def part1(calorie_list: List[str]) -> int:
    return max(calorie_list)


def part2(calorie_list: List[str]) -> int:
    sorted_list = sorted(calorie_list, reverse=True)
    return sorted_list[0] + sorted_list[1] + sorted_list[2]


def main():
    data = read_file_by_line('input.txt')
    calorie_list = calculate_calorie_list(data)
    print(f'part 1: {part1(calorie_list)}')
    print(f'part 2: {part2(calorie_list)}')


if __name__ == "__main__":
    main()
