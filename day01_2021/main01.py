with open('input.txt', 'r') as f:
    lines = f.readlines()
    raw_data = [int(entry.strip()) for entry in lines]

count = sum(
    raw_data[i] > raw_data[i - 1]
    for i in range(1, len(raw_data))
)

print(f'part 1: {count}')

count = sum(
    raw_data[i] > raw_data[i - 3]
    for i in range(1, len(raw_data))
)

print(f'part 2: {count}')

