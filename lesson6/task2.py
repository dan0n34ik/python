class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weigh(self, one_weigh, thickness):
        return f'{(self._length * self._width * one_weigh * thickness) / 1000} т'


my_road1 = Road(20, 5000)

print(my_road1.weigh(25, 5))
