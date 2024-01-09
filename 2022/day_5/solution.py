# importing the data
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/input.txt') as file:
    input = file.read()


original = input.split('move')[0]
instructions = input.split('move')[1:]
instructions = [x.split() for x in instructions]
instructions = [[item for item in sublist if item.isdigit()]
                for sublist in instructions]

print("original:\n\n", original)
# print("instructions:\n\n", instructions)


# Part 1
# Move boxes between positions

number_of_stack = max([int(x) for x in original if x.isdigit()])
res = [[] for _ in range(number_of_stack)]

# putting the boxes in their stacks
for i, k in enumerate(original):
    if original[(i*4)+1].isdigit():
        break
    if original[(i*4)+1].isalpha():
        # print(i % number_of_stack, original[(i*4)+1])
        res[i % number_of_stack].append(original[(i*4)+1])
        # print("inserted:", original[(i*4)+1],
        #       "in stack: ", i % number_of_stack+1, "index: ", i)

# print("starting: ", res)

# moving the boxes
# i[0] = boxes to move
# i[1] = from stack
# i[2] = to stack

for i in instructions:
    boxes_to_move = int(i[0])
    from_stack = int(i[1])-1
    to_stack = int(i[2])-1
    # print("instructions: ", boxes_to_move, from_stack+1, to_stack+1)
    for _ in range(boxes_to_move):
        res[to_stack].insert(0, res[from_stack].pop(0))
    # print(
    #     f"After: moving {boxes_to_move} from {from_stack+1} to {to_stack+1}\n", res)

# print(res)
print("Part 1: ", end="")
for stack in res:
    print(stack[0], end="")
