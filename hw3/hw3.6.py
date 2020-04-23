def int_func():
    text=input('Введите слово,состоящее из латинских букв c маленькой буквы: ')
    return text.capitalize()


def new_func():
    o=True
    new_text = []
    while True:
        if int_func()=='Q' or int_func()=='q':
            o=False
            break
        else:
            new_text.append(int_func())
    return new_text

print(new_func())