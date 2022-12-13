with open("Day4input.txt", "r") as file:
    assignments=file.read().split("\n")
total = 0
for item in assignments:
    zone_list = item.split(",")
    first_elf=zone_list[0].split("-")
    second_elf=zone_list[1].split("-")
    first_elf = list(range(int(first_elf[0]), int(first_elf[1])+1))
    second_elf= list(range(int(second_elf[0]), int(second_elf[1])+1))
    if any(num in first_elf for num in second_elf):
        total+=1
print(total)
        
