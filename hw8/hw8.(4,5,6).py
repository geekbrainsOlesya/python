class Storage:
    equip_store=[]



class Equipment(Storage):

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount


    def reception(self):
        self.stor = []
        self.stor.append(self.name+','+ str(self.price)+ 'р.'+ ',' + str(self.amount)+'шт')
        print(self.stor)

    def deliver_to_store(self):
        self.equip_store.append(self.stor)

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.amount}'

    @classmethod
    def valid(cls, self):
        try:
            self.amount=int(self.amount)
            self.price=int(self.price)
        except TypeError:
            return 'Неправильный тип данных!'







class Printer(Equipment):
    def Speed(self,speed):
        self.speed=30
        return f'Скорость печати {speed}'


class Scanner(Equipment):
    def Speed(self, speed):
        self.speed = 40
        return f'Скорость сканирования {speed}'


class Copier(Equipment):
    def Speed(self, speed):
        self.speed = 20
        return f'Скорость копирования {speed}'


a=Equipment('LG', 5600, 6)
a.reception()
a.deliver_to_store()
c=Equipment('Samsung', 6800, 3)
c.reception()
c.deliver_to_store()
b=Storage
print(b.equip_store)
