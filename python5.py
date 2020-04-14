revenue = int(input('Выручка фирмы: '))
costs = int(input('Издержки фирмы: '))
result = revenue - costs

if revenue > costs:
    print('Прибыль фирмы: ' + str(result))
    rentab = result / revenue
    print('Рентабельность: ' + str(rentab))
    employee = int(input('Введите количество сотрудников: '))
    salary = result / employee
    print('Прибыль на одного сотрудника: ' + str(salary))
elif revenue < costs:
    print('Убыток фирмы: ' + str(result))
else:
    print('Издержки и выручка равны')
