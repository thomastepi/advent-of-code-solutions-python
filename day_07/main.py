from utils import read_file_by_line


def create_file_list(instructions):
    file_list = {}
    current_line = 0
    current_location = '/'
    while current_line < len(instructions):
        current_instruction = instructions[current_line]
        if current_instruction == 'cd /':
            current_location = '/'
            current_line += 1
        elif current_location == 'cd ..':
            current_location = '/'.join(current_location.split('/')[:-1])
            current_line += 1
        elif 'cd' in current_line:
            current_location = f'{current_location}/{current_line.split(' ')[1]}'

    return file_list


def main():
    instructions = read_file_by_line('test.txt')
    file_list = create_file_line(instructions)
    folder_list = create_folder_list(file_list)
    print(f'part 1: {part1(folder_list)}')


if __name__ == '__main__':
    main()