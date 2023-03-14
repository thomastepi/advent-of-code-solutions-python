from typing import List


def read_file_by_line(filename: str) -> List[str]:
    out = []
    with open(filename, 'r') as file:
        for line in file:
            out.append(line.replace('\n', ''))
    return out


def read_file_and_split(filename: str, divider: str) -> List[List[str]]:
    out = []
    with open(filename, 'r') as file:
        for line in file:
            out.append(line.replace('\n', '').split(divider))
    return out


def read_line_from_file(filename: str, line_number: int) -> str:
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            count += 1
            if count == line_number:
                return line
