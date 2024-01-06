import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt') as file:
    input = file.read()

input = input.split('\n')
elves = []
total = 0

for i in input:
    if i == '':
        elves.append(total)
        total = 0
        continue
    total += int(i)

# part 1 solution
print(max(elves))

# part 2 solution
elves.sort()
print(sum(elves[-3:]))
