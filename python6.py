a=int(input('Результат в 1ый день (км): '))
b=int(input('Нужный резульат (км): '))
day=1

while a<b:
    a+=a/100*10
    day+=1
print(f'На {day}-й день спортсмен достиг результата - не менее {b} км')