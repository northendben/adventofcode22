with open("Day8input.txt", "r") as file:
    data= file.read().split("\n")
grid_dict = {}
for num in range(0,len(data)):
    grid_dict[num] = data[num]
score_list = []
import pdb
for count,item in enumerate(data):
    for index,char in enumerate(item):
        up_compare = None
        down_compare = None
        right_compare = None
        left_compare = None
        if count < 100:
            keep_going=True
            down_compare = [int(num[index])for num in list(grid_dict.values())[count+1:]] #get all dict values below this one in
            if count > 0:
                up_compare = [int(num[index]) for num in list(grid_dict.values())[:count]][::-1]
            if index > 0:
                left_compare = [int(num) for num in data[count][:index]][::-1]
            right_compare = [int(num) for num in data[count][index+1:]]
            totals= []
            for compare in down_compare, up_compare, right_compare, left_compare:
                total = 0
                # pdb.set_trace()
                if compare:
                    for item in compare:
                        if item < int(char):
                            total+=1
                        elif item == int(char) or item > int(char):
                            total+=1
                            break 
                    totals.append(total)
            total = 1
            if all(item == 0 for item in totals):
                total = 0
            else:   
                for item in totals:
                    if item > 0:
                        total = item*total   
            score_list.append(total)
print(max(score_list))
