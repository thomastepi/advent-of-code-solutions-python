from utils import read_line_from_file


def no_duplicates(data):
    return len(set(data)) == len(data)


def part1(raw, window_size):
    for i in range(window_size, len(raw)+1):
        window = raw[i-window_size:i]
        if no_duplicates(window):
            return i


def main():
    raw = read_line_from_file('input.txt', 1)
    print(f'part 1: {part1(raw, 4)}')
    print(f'part 2: {part1(raw, 14)}')


if __name__ == '__main__':
    main()