class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def calc(self, _length, _width):
            res = _length * _width * 25 * 5
            res=int(res / 1000)
            print(str(res)+'т')



a = Road(20, 5000)
a.calc(20,5000)
