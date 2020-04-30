with open('text_3.txt', 'r') as people:
    people = people.read().split('\n')
    print(people)
    salary = []
    poor = []

    for i in people:
        i = i.split(' ')
        if float(i[1]) < 20000.0:
            poor.append(i[0])
        salary.append(i[1])

    print(f'Оклад меньше 20.000:  {poor}, средний оклад:  {sum(map(float, salary)) / len(salary)}')
