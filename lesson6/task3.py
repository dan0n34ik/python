class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker1 = Position('Ivan', 'Ivanov', 'Boss', {'wage': 100000, 'bonus': 10000})

print(worker1.get_full_name())
print(worker1.get_total_income())
