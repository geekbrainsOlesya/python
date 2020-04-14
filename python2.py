seconds = int(input('Введите время в секундах: '))
h = seconds // 3600
m = (seconds - 3600 * h) // 60
s = seconds - h * 3600 - m * 60

if h < 10:
    h = '0' + str(h)
    if m < 10:
        m = '0' + str(m)
        if s < 10:
            s = '0' + str(s)
print(f'{h}:{m}:{s}')
