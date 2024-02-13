list = [133,44,222,55]
max = list[0]
min = list[0]
# print(max(list))
# print(min(list))

# to find minimum number
for i in list:
    if i < min: 
        min = i

print(min)

# to Find largest Number
for i in list:
    if i > max: 
        max = i

print(max)

