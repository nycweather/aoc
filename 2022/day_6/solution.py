import os

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/input.txt') as file:
    input = file.read()

# part 1 find first 4 unique characters in a set of 4
for i in range(0, len(input)-4):
    table = set(input[i:i+4])
    if len(table) == 4:
        print(i+4)
        break


# part 2 same as part 1 but with 14 characters
for i in range(0, len(input)-14):
    table = set(input[i:i+14])
    if len(table) == 14:
        print(i+14)
        break
