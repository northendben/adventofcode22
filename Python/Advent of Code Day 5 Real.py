import re
import pdb
with open("Day5input.txt") as file:
    data=file.read().replace("    ", "None,").replace("]",",").replace("[","").replace(" ","").split("\n")
key_list = []
format_list = []
for line in data:
    x = line.split(",")
    format_list.append(x)
keys = format_list.pop()
key_list= [int(char) for char in keys[0]]
stack_dict = dict.fromkeys(key_list,None)
for item in stack_dict:
    stack_dict[item] = []

final_list = []
for stack in format_list:
    hold_list = []
    for count,box in enumerate(stack,start=1):
        if box != "None" and box != "":
            stack_dict[count].insert(0,box)


with open("Day5instructions.txt", "r") as file:
    data=file.read().split("\n")
instructions = []
regex = re.compile(r'(\d+)')
for item in data:
    matches = regex.findall(item)
    for count,item in enumerate(matches):
        matches[count] = int(item)
    instructions.append(matches)


for item in instructions:
    # pdb.set_trace()
    count = 0
    box_count = item[0]
    from_stack = item[1]
    to_stack = item[2]
    while count < box_count:
        box_being_moved = stack_dict[from_stack].pop()
        stack_dict[to_stack].append(box_being_moved)
        count+=1
        print(stack_dict)
        
print(stack_dict)
answer = [char[-1] for char in list(stack_dict.values())]
answer = "".join(answer)
print(answer)
