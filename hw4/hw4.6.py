from itertools import count
from itertools import cycle


# for el in count(4):
#     if el > 15:
#         break
#     else:
#         print(el)

#*******************************************
# c = 0
# for el in cycle("ABC"):
#     if c > 10:
#         break
#     print(el)
#     c += 1
#***************** СОВМЕЩЕННОЕ РЕШЕНИЕ******

def my_func():
    smth = input('Введите строку или число- ').split()
    if smth[0] == '1' or smth[0] == '2' or smth[0] == '3' or smth[0] == '4' or smth[0] == '5'or smth[0] == '6' or smth[0] == '7' or smth[0] == '8' or smth[0] == '9' or smth[0] == '0':
        smth=int(smth[0])
        for el in count(smth):
            if el > smth+100:
                break
            else:
                print(el)
    else:
        c=0
        for el in cycle(smth):
            if c > 10:
                break
            else:
                print(el)
                c += 1


my_func()





