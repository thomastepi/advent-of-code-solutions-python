from utils import read_file_by_line


def parse_line(line):
    out = []
    for r in line.split(','):
        numbers = r.split('-')
        out.append(range(int(numbers[0]), int(numbers[1])+1))
    return out


def total_overlap(ranges):
    intersection = set(ranges[0]).intersection(ranges[1])
    return len(intersection) == min(len(ranges[0]), len(ranges[1]))


def has_overlap(ranges):
    return len(set(ranges[0]).intersection(ranges[1])) > 0


def part1(raw_input):
    out = 0
    for line in raw_input:
        ranges = parse_line(line)
        if total_overlap(ranges):
            out += 1
    return out


def part2(raw_input):
    out = 0
    for line in raw_input:
        ranges = parse_line(line)
        if has_overlap(ranges):
            out += 1
    return out


def main():
    raw_input = read_file_by_line('input.txt')
    print(f"Part 1: {part1(raw_input)}")
    print(f"Part 2: {part2(raw_input)}")


if __name__ == "__main__":
    main()
