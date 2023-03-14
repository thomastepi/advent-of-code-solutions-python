from utils import read_file_by_line


def get_priority(letter):
    if letter.islower():
        return ord(letter) - ord('a') + 1
    if letter.isupper():
        return ord(letter) - ord('A') + 27


def get_intersection(bags):
    unique = set(bags[0])
    for b in range(1, len(bags)):
        unique = unique.intersection(bags[b])
    return unique.pop()


def part1(bags):
    out = 0
    for bag in bags:
        temp = [bag[:len(bag) // 2], bag[len(bag) // 2:]]
        out += get_priority(get_intersection(temp))
    return out


def part2(bags):
    out = 0
    for b in range(0, len(bags), 3):
        temp = bags[b:b+3]
        out += get_priority(get_intersection(temp))
    return out


def main():
    bags = read_file_by_line('input.txt')
    print(f'part 1: {part1(bags)}')
    print(f'part 1: {part2(bags)}')


if __name__ == '__main__':
    main()