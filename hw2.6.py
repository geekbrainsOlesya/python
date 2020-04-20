name_1 = input('Введите название товара №1')
name_2 = input('Введите название товара №2')
name_3 = input('Введите название товара №3')

price_1 = int(input('Введите цену тавара №1'))
price_2 = int(input('Введите цену тавара №2'))
price_3 = int(input('Введите цену тавара №3'))

amount_1 = int(input('Введите количество товаров №1'))
amount_2 = int(input('Введите количество товаров №2'))
amount_3 = int(input('Введите количество товаров №3'))

unit_1 = input('Введите единицу измерения товара №1')
unit_2 = input('Введите единицу измерения товара №2')
unit_3 = input('Введите единицу измерения товара №3')

my_list = [
    (1, {'название': '', 'цена': '', 'количество': '', 'eд': ''}),
    (2, {'название': '', 'цена': '', 'количество': '', 'eд': ''}),
    (3, {'название': '', 'цена': '', 'количество': '', 'eд': ''})
]

one = ((list(my_list[0]))[1])
two = ((list(my_list[1]))[1])
three = ((list(my_list[2]))[1])

one['название'] = name_1
one['цена'] = price_1
one['количество'] = amount_1
one['ед'] = unit_1

two['название'] = name_2
two['цена'] = price_2
two['количество'] = amount_2
two['ед'] = unit_2

three['название'] = name_3
three['цена'] = price_3
three['количество'] = amount_3
three['ед'] = unit_3

new_list = one,two,three
x=list(new_list)
result=[1,x[0]]+[2,x[1]]+[3,x[2]]
print(result)

list_one= [one.get('название'),two.get('название'),three.get('название')]
list_two = [one.get('цена'), two.get('цена'), three.get('цена')]
list_three= [one.get('количество'), two.get('количество'), three.get('количество')]
list_four=[one.get('ед'), two.get('ед'), three.get('ед')]

my_dict=dict( название = list_one ,
              цена = list_two,
              количество= list_three,
              ед= list_four
              )
print(my_dict)



