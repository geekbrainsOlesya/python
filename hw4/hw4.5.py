from functools import reduce

numbers = [i for i in range(100, 1000 + 1) if i % 2 == 0]


def my_func(prev_el, el):
    return prev_el * el


print(f'Четные числа-{numbers}')
print(f'Произведение всех чисел в списке-{reduce(my_func, (numbers))}')
