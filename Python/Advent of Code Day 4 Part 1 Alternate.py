with open("Day4input.txt", "r") as file:
    assignments=file.read().split("\n")
total = 0
for item in assignments:
    zone_list = item.split(",")
    first_elf = set(list(map(lambda x: range(int(x[0]),int(x[1])+1),[item.split("-") for item in zone_list]))[0])
    second_elf = set(list(map(lambda x: range(int(x[0]),int(x[1])+1),[item.split("-") for item in zone_list]))[1])
    print(first_elf)
    print(second_elf)
    if first_elf.issubset(second_elf) or second_elf.issubset(first_elf):
        total+=1
print(total)