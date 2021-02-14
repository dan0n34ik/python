class Sklad:
    def __init__(self):
        self.max_boxes = 100000


class OrgTechnic:
    def __init__(self, max_sheets, razreshenie):
        self.max_sheets = max_sheets
        self.razreshenie = razreshenie
        self.boxes_used = 0
        self.data = []

    def peredacha_na_sklad(self, kolichestvo, type_of_technic, code):
        try:
            self.boxes_used += int(kolichestvo)
        except ValueError:
            print('Количество надо вводить цифрами!')
            return ''
        if self.boxes_used > Sklad().max_boxes:
            print('Склад заполнен!')
            return ''
        if type_of_technic != 'принтер' and type_of_technic != 'сканер' and type_of_technic != 'ксерокс' and \
                type_of_technic != 'printer' and type_of_technic != 'scanner' and type_of_technic != 'copir':
            print('Можно добавлять только принтер, сканер или ксерокс.')
            return ''
        self.data.append({'тип': type_of_technic, 'код': code, 'количесто': kolichestvo})


class Printer(OrgTechnic):
    def __init__(self, max_sheets, razreshenie, pechat_fotografiy, types_of_files):
        super().__init__(max_sheets, razreshenie)
        self.pechat_fotografiy = pechat_fotografiy
        self.types_of_files = types_of_files


class Scanner(OrgTechnic):
    def __init__(self, max_sheets, razreshenie, metod_of_scanning):
        super().__init__(max_sheets, razreshenie)
        self.metod_of_scanning = metod_of_scanning


class Copir(OrgTechnic):
    def __init__(self, max_sheets, razreshenie, copies_in_cycle):
        super().__init__(max_sheets, razreshenie)
        self.copies_in_cycle = copies_in_cycle


my_printer = Printer(70, '1200x1200', True, ['PDF', 'JPG'])
my_scanner = Scanner(135, '600x600', 'Сканирование Push')
my_copir = Copir(70, '60x600', 999)

my_printer.peredacha_na_sklad('70001', 'printer', '116z75x5y8jg94')
my_printer.peredacha_na_sklad('123', 'printer', '1213kjh865jg46')
my_scanner.peredacha_na_sklad(70000, 'scanner', '16sfs7485hll07')
print(my_scanner.data)
print(my_printer.data)
