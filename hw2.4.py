text = input('Введите фразу из нескольких слов: ')

x = text.split()
print(x)

for i in enumerate(x):
    print(i)
