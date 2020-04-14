n = int(input('Введите многозначное число: '))
max = 0

while n>0:
    try_n = n % 10
    n = n // 10
    if try_n > max:
        max = try_n

print(max)
