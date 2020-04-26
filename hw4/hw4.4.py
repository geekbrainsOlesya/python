numbers = [3, 4, 4, 6, 4, 7, 22, 76, 22]
new_nums = [i for i in numbers if numbers.count(i) == 1]
print(new_nums)
