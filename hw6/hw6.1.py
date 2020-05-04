from time import sleep


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый', 'желтый']

    def running(self):
        while True:
            tm = [7, 2, 5, 2]
            x = 0
            for i in self.__color:
                a = i
                print(a)
                sleep(tm[x])
                x += 1


a = TrafficLight()
a.running()
