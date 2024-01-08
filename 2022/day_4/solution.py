import os


dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt') as file:
    input = file.read()

input = input.split("\n")

# Part 1

# if one elf's assignment is a subset of its partner's assignment
def part1(input):
    count = 0
    for group in input:
        elf_1_start, elf_1_end = group.split(",")[0].split("-")
        elf_2_start, elf_2_end = group.split(",")[1].split("-")
        if int(elf_1_start) <= int(elf_2_start) and int(elf_1_end) >= int(elf_2_end):
            count += 1
        elif int(elf_2_start) <= int(elf_1_start) and int(elf_2_end) >= int(elf_1_end):
            count += 1
    print(count)

print("Part 1")
part1(input)

# Part 2

# if one elf's assignment overlaps with its partner's assignment

def part2(input):
    count = 0
    for group in input:
        elf_1_start, elf_1_end = group.split(",")[0].split("-")
        elf_2_start, elf_2_end = group.split(",")[1].split("-")
        if int(elf_1_start) <= int(elf_2_start) and int(elf_1_end) >= int(elf_2_start):
            count += 1
        elif int(elf_2_start) <= int(elf_1_start) and int(elf_2_end) >= int(elf_1_start):
            count += 1
    print(count)

print("Part 2")
part2(input)