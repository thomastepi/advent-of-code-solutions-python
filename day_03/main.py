from utils import read_file_by_line, read_file_and_split
from string import ascii_letters

# load raw data
data = read_file_by_line('input.txt')

# iterate through each item and divide into 2 equal parts
sum_of_priorities = 0
for item in data:
    midway = (len(item)) // 2
    left = set(item[:midway])
    right = set(item[midway:])

    # get priority character and sum
    for priority, xter in enumerate(ascii_letters):
        if xter in left and xter in right:
            sum_of_priorities += priority + 1

print(f'part 1: {sum_of_priorities}')


# part 2
j = 3
sum_of_priorities = 0

# isolate groups of 3 elves each
for i in range(0, len(data), 3):
    group = data[i:j]
    j += 3

# find item common to all 3 rucksacks in each group and get the sum
    for priority, xter in enumerate(ascii_letters):
        if xter in group[0] and xter in group[1] and xter in group[2]:
            sum_of_priorities += priority + 1

print(f'part 2: {sum_of_priorities}')







