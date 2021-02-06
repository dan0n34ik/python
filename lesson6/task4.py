import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is going with speed {self.speed}')

    def stop(self):
        print(f'{self.name} has just stopped')

    def turn(self, direction):
        if direction == 1:
            print(f'{self.name} has turned on the left')
        elif direction == 2:
            print(f'{self.name} has turned on the right')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('The speed of a town car must be less than 60!!!')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('The speed of a work car must be less than 40!!!')


class PoliceCar(Car):
    def p_police(self):
        print('This car is police.')


class SportCar(Car):
    def drift(self):
        print('shhhhhhhhhhhhhhhhh!!!')


town_car1 = TownCar(65, 'red', 'Lada', False)
town_car1.show_speed()
print()
work_car1 = WorkCar(45, 'white', 'Mazda', False)
work_car1.show_speed()
print()
police_car1 = PoliceCar(100, 'blue', 'Reno', True)
police_car1.p_police()
print()
sport_car1 = SportCar(150, 'green', 'Ferrari', False)
sport_car1.drift()
