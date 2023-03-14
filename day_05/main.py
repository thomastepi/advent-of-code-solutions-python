from utils import read_file_by_line, read_file_and_split
from typing import List


def parse_instructions(instructions: str) -> (int, int, int):
    out = instructions.split(' ')
    return int(out[1]), int(out[3]) - 1, int(out[5]) - 1


def get_tops(state: List[List[str]]) -> str:
    out = ''
    for pile in state:
        out += pile[0]


def part1(state: List[List[str]], instructions: List[str]) -> str:
    for instruction in instructions:
        count, start, end = parse_instructions(instruction)
        for i in range(0, count):
            temp = state[start].pop(0)
            state[end].insert(0, temp)
    return get_tops(state)


def part2(state: List[List[str]], instructions: List[str]) -> str:
    for instruction in instructions:
        count, start, end = parse_instructions(instruction)
        temp = state[start][:count]
        state[start] = state[start][count:]
        temp.extend(state[end])
        state[end] = temp
    return get_tops(state)


def main():
    instructions = read_file_by_line('test_instructions.txt')
    start_state = read_file_and_split('test_state.txt', ',')
    print(f'part 1: {part1(start_state, instructions)}')
    start_state = read_file_and_split('test_state.txt', ',')
    print(f'part 2: {part2(start_state, instructions)}')


if __name__ == '__main__':
    main()
