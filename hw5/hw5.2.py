with open('file_1.txt', 'r') as okey:
    lines = len(okey.readlines())
    print(f'Количество строк в файле: {lines}')

    for line in range(lines):
        print(f'Количество слов в строке №{line + 1}:  ')
