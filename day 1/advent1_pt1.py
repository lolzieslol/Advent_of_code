filpath = 'day 1/real_input.txt'
fil = open(filpath,encoding='utf-8')
content = fil.read()
list1 = []
list2 = []

lines = content.split('\n')

for line in lines:
    if len(line) < 4:
        continue
    
    row = line.split('   ')
    if len(row) != 2:
        continue
    
    list1.append(int(row[0]))
    list2.append(int(row[1]))


rounds = len(lines)
print(rounds)
differences = []
for i in range(rounds):
    differences.append(abs(min(list1) - min(list2)))
    list1.remove(min(list1))
    list2.remove(min(list2))
    if len(list1) == 0:
        print(i)
        break

total_distance = 0
for distance in differences:
    total_distance += distance

print(total_distance)