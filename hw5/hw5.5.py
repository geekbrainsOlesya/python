with open('text_5.txt', 'w') as txt5:
    nums=input('Введите числа через пробел- ')
    txt5.write(nums)
    my_n=nums.split()
    print(f'Сумма чисел: {sum(map(int, my_n))}')






