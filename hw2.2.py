ls = []
el = input('Введите 6 элементов для создания списка : ')
ls.extend(el.replace(' ', ''))
print(ls)
a = ls[:2]
b = ls[2:4]
c = ls[4:6]
print(a[::-1] + b[::-1] + c[::-1])
