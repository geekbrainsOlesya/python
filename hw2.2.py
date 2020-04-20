ls = []
el = input('Введите 6 элементов для создания списка : ')
ls.extend(el.replace(' ', ''))
print(ls)
a = ls[:2]
b = ls[2:4]
c = ls[4:6]
print(a[::-1] + b[::-1] + c[::-1])

# ls = []
# el = input('Введите элементы для создания списка : ')
# ls.extend(el.replace(' ', ''))
#
# for i in range(len(ls)):
#     new_list = []
#     rv = ls[i:i + 2]
#     new_list.append(rv[::-1])
#     i+=2
# print(new_list)


# ls = []
# el = input('Введите элементы для создания списка : ')
# ls.extend(el.replace(' ', ''))
#
# for i in range(len(ls)):
#     new_list = []
#     ls[i],ls[i+1]=ls[i+1],ls[i]
#     new_list.append(ls)
#     i+=2
# print(new_list)
