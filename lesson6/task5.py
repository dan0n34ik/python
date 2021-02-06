class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Ручкой написали "\033[3mПривет, мир!\033[0m"')


class Pencil(Stationery):
    def draw(self):
        print('Карандашом нарисовали "\*_*/"')


class Handle(Stationery):
    def draw(self):
        print('Маркером написали жирно "\033[1mПривет, мир\033[0m"')


my_pen = Pen('pen')
my_pen.draw()
print()
my_pencil = Pencil('pencil')
my_pencil.draw()
print()
my_handle = Handle('handle')
my_handle.draw()
