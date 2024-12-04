
input_file = open('day 2/real_input.txt',encoding='utf-8')
inputs = input_file.read()
input_file.close()

report_safety = []

reports = inputs.split('\n')

for report in reports:
    if len(report) < 4:
        continue

    levels = report.split()
    
    decreasing  = False
    increasing = False
    big_jump = False
    
    i = 0
    while i<(len(levels)-1):
        old_level = int(levels[i])
        new_level = int(levels[i+1])
        if new_level < old_level:
            decreasing  = True
        
        if new_level > old_level:
            increasing = True
        
        if abs(new_level - old_level) not in [1,2,3]:
            big_jump = True
        
        i+=1
    
    print(decreasing ,increasing,big_jump)
    if decreasing  == increasing or big_jump == True:
        report_safety.append('Unsafe')
    else:
        report_safety.append('Safe')

print(report_safety.count('Safe'))