class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        if self.is_police == True:
            d = 'направо'
        else:
            d = 'налево'
        print('Машина повернула ' + d)

    def show_speed(self):
        print('Текущая скорость автомобиля: ' + str(self.speed) + 'км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Разрешенная скорость превышана на ' + (str(self.speed - 60))+ ' км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Разрешенная скорость превышена на ' + str(self.speed - 40) + ' км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


a = SportCar(290, 'red', 'Bugatti', True)
a.go()
a.show_speed()
b = WorkCar(66, 'white', 'Mercedes', False)
b.go()
b.turn()
b.show_speed()
k = TownCar(79, 'black', 'Range Rover', True)
k.go()
k.show_speed()
h = PoliceCar(45, 'Yellow', 'Lada Granta', True)
