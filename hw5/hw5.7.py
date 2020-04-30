import json

with open('text_7.txt', 'r') as txt:
    rd = txt.readlines()
    my_dict = []
    for line in rd:
        name, firm, income, costs = line.split()
        d = {name: int(income) - int(costs) for line in rd}
        my_dict.append(d)
    summa = (my_dict[0]['Brooms'] + my_dict[2]['Honey-cake'] + my_dict[3][
        'Matrioshka'] - my_dict[4]['Сказка']) / 4
    my_dict.append({'Средняя прибыль компаний': summa})
    print(my_dict)

with open("my_file.json", "w") as write_f:
    json.dump(my_dict, write_f,ensure_ascii=False,indent=2)
