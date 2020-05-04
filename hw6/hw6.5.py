class Stationery:
    def __init__(self, title):
        self.title=title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки. Используется: '+ self.title)


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки. Используется: '+ self.title)


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки. Используется: '+ self.title)

a=Pen('ручка')
a.draw()
b=Pencil('карандаш')
b.draw()
h=Handle('маркер')
h.draw()