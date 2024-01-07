import os

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt') as file:
    input = file.read()

input = input.split("\n")
updated_input = []

for rucksack in input:
    rucksack = rucksack.strip()
    temp1 = rucksack[0:len(rucksack)//2]
    temp2 = rucksack[len(rucksack)//2:]
    updated_input.append((temp1, temp2))

vals_from_input = []

for rucksack in updated_input:
    temp = set()
    first_half = set(list(rucksack[0]))
    for letter in rucksack[1]:
        if letter in first_half:
            temp.add(letter)

for rucksack in updated_input:
    temp = set()
    first_half = set(list(rucksack[0]))
    for letter in rucksack[1]:
        if letter in first_half:
            temp.add(letter)

    vals_from_input.extend(temp)


final_vals = []
for letter in vals_from_input:
    if letter in lower:
        final_vals.append(ord(letter)-96)
    else:
        final_vals.append(ord(letter)-65+27)

# print(vals_from_input)
# print((final_vals))
print(sum(final_vals))


## Part 2
sol_2_input = []

for rucksack in range(0, len(input), 3):
    temp = []
    for i in range(3):
        temp.append(input[rucksack+i])
    sol_2_input.append(temp)

# print(sol_2_input)
vals_from_sol_2_input = []

for group in sol_2_input:
    temp1 = set()
    temp2 = set()
    temp3 = set()
    for letter in group[0]:
        temp1.add(letter)
    for letter in group[1]:
        if letter in temp1:
            temp2.add(letter)
    for letter in group[2]:
        if letter in temp2:
            temp3.add(letter)
    vals_from_sol_2_input.extend(temp3)

# print(vals_from_sol_2_input)

final_vals_sol_2 = []

for letter in vals_from_sol_2_input:
    if letter in lower:
        final_vals_sol_2.append(ord(letter)-96)
    else:
        final_vals_sol_2.append(ord(letter)-65+27)

print(sum(final_vals_sol_2))