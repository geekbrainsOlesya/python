class Data:
    @classmethod
    def transform(cls):
        num=cls.valid()
        try:
            n=f'{int(num[0])}.{int(num[1])}.{int(num[2])}'
        except TypeError:
            print('Ошибка!')
        else:
            print(n)


    @staticmethod
    def valid():
        date=input('Введите дату в формате день-месяц-год: ')
        try:
            date_list=date.split('-')
            if not (1<= int(date_list[0])<=31) and (1<=int(date_list[1])<=12) and (0 <=int(date_list[2])<=2020):
              print('Неверный формат ввода')
        except ValueError:
            return None
        else:
            return date_list

a=Data()
a.transform()