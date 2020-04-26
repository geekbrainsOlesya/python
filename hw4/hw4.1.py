from sys import argv

file_name, hours, wage_rate, bonus = argv
try:
    salary = int(hours) * int(wage_rate) + int(bonus)
    print(f'Зарплата сотрудника составляет-{salary}')
except ValueError:
    print('Вы ввели не цифровое значение')
