def division_2(dividend, divider):
    try:
        res = dividend / divider
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    return res


x = int(input('Введите число-делимое: '))
y = int(input('Введите число-делитель: '))

print(division_2(x, y))


# ****************************************************


def division(*args):
    try:
        num_1 = int(input('Введите число-делимое: '))
        num_2 = int(input('Введите число-делитель: '))
        result = num_1 / num_2
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    return result


print(division())
