import re

my_dict = {}
with open('text_6.txt') as file:
    lines = file.readlines()
    for line in lines:
        splitt = line.split(':')
        subj = splitt[0]
        sum_lessons = sum([int(num) for num in (re.findall('\d+', splitt[1]))])
        my_dict[subj] = sum_lessons
print(my_dict)
