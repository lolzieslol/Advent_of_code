
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



# uniques1 = set(list1)
score = 0
for number in list1:
    score += number * list2.count(number) 

print(score)