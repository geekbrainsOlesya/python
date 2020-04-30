my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_f = []
with open("text_4.txt", "r") as my_f:
    for i in my_f:
        i = i.split(' ', 1)
        new_f.append(my_dict[i[0]] + '  ' + i[1])
    print(new_f)

with open('text_4_new.txt', 'w') as my_f_new:
    my_f_new.writelines(new_f)


