with open('file_1.txt', 'w') as okey:
    while True:
        data = input('Введите данные построчно: \nДля завершения нажмите Enter.')
        if data != '':
            okey.write(data + '\n')
        else:
            break
