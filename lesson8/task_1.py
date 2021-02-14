class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date(cls, date):
        date_li = cls(date).date.split()
        cls.day, cls.month, cls.year = int(date_li[0]), int(date_li[1]), int(date_li[2])

    @staticmethod
    def validation(obj):
        if obj.day > 31 or obj.day < 1:
            print('Числа больше 31 или меньше 1 не бывает!!!')
        if obj.month < 1 or obj.month > 12:
            print('Месяца больше 12 или меньше 1 не бывает!!!')
        if obj.year < 1:
            print('До нашей эры...')


date_from_user = input('Введите дату в формате "день месяц год": ')
my_date = Date(date_from_user)
my_date.get_date(my_date.date)
my_date.validation(my_date)
print(my_date.day, my_date.month, my_date.year)
