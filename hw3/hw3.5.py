
def sum_of_num():
    o = True
    last_result = 0
    while o == True:
        numbers = input('Введите числа разделенные пробелом или Q для выхода: ').split()
        result = 0
        for n in range(len(numbers)):
            if numbers[n] == 'q' or numbers[n] == 'Q':
                o = False
                break
            else:
                result += int(numbers[n])
        last_result += result
        print(f'Cумма = {last_result}')
    print(f'Конечная сумма = {last_result}')


sum_of_num()
