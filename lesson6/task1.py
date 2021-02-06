from time import sleep


class TrafficLight:
    __color = 'красный'

    def running(self):
        if self.__color == 'красный':
            for i in range(7, 0, -1):
                print(f'\x1b[31m{self.__color} цвет будет ещё {i} секунды\x1b[0m')
                sleep(1)
            self.__color = 'жёлтый'
            print()
        if self.__color == 'жёлтый':
            for i in range(2, 0, -1):
                print(f'\033[93m{self.__color} цвет будет ещё {i} секунды\033[0m')
                sleep(1)
            self.__color = 'зелёный'
            print()
        if self.__color == 'зелёный':
            for i in range(5, 0, -1):
                print(f'\033[92m{self.__color} цвет будет ещё {i} секунды\033[0m')
                sleep(1)
            self.__color = 'красный'
            print()


my_traffic_light = TrafficLight()
while True:
    my_traffic_light.running()
