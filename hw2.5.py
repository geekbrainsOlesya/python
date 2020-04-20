number_list = [9, 6, 6, 3, 1]
el = int(input('Введите новый элемент списка: '))


for i in number_list:
    if el < number_list[i]:
        i += 1
    else:
        number_list.insert(i, el)
print(number_list)
