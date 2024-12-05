class Books:
    material = 'бумага'
    text_av = True
    reserved = False

    def __init__(self, name, author, page_quantity, isbn, reserved):
        self.name = name
        self.author = author
        self.page_quantity = page_quantity
        self.isbn = isbn
        self.reserved = reserved

    def print(self):
        s_reserved = ''
        if self.reserved:
            s_reserved = ', зарезервировано'

        print(f'Название: {self.name}, Автор: {self.author}, '
              f'страниц: {self.page_quantity}, материал: {self.material}'
              f'{s_reserved}')


class TextBook(Books):
    home_work = False

    def __init__(self, name, author, page_quantity, item, school_class,
                 home_work, isbn, reserved):
        super().__init__(name, author, page_quantity, isbn, reserved)
        self.name = name
        self.author = author
        self.page_quantity = page_quantity
        self.item = item
        self.school_class = school_class
        self.home_work = home_work
        self.reserved = reserved

    def print(self):
        s_home_work = ''
        if self.home_work:
            s_home_work = 'есть'
        else:
            s_home_work = 'нет'
        s_reserved = ''
        if self.reserved:
            s_reserved = ', зарезервировано'

        print(f'Название: {self.name}, Автор: {self.author}, '
              f'страниц: {self.page_quantity}, предмет: {self.item}, '
              f'класс: {self.school_class}, домашнее задание: '
              f'{s_home_work}{s_reserved}')


first_book = Books('Психология народов и масс', 'Г. Лебон',
                   383, 978 - 5 - 17 - 101642 - 5, True)
second_book = Books('Пропаганда', 'Э. Бернейс',
                    220, 978 - 5 - 4461 - 1857 - 1, False)
third_book = Books('Поправка - 22', 'Дж. Хеллер',
                   733, 978 - 5 - 1, False)
fourth_book = Books('1984', 'Дж. Оруэлл',
                    319, 978 - 5 - 17, False)
fifth_book = Books('Колымские рассказы', 'В. Шаламов',
                   412, 978 - 5 - 389 - 24121 - 3, False)
first_text_book = TextBook('Алгебра', 'Иванов', 222,
                           'Математика', 6, False, 888, False)
second_text_book = TextBook('Русский язык', 'Петров', 386,
                            'Русский язык', 7, True, 777, True)
third_text_book = TextBook('Биология', 'Сидоров', 400,
                           'Биология', 11, True, 4444, False)

first_book.print()
second_book.print()
third_book.print()
fourth_book.print()
fifth_book.print()
first_text_book.print()
second_text_book.print()
third_text_book.print()
