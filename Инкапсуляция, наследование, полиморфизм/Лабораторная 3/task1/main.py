class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("Ошибка. name должен быть str")
        self.__name = name

        if not isinstance(author, str):
            raise TypeError("Ошибка. author должен быть str")
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f"Книга {self.name!r}. Автор {self.author!r}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError("Ошибка. pages должен быть int")
        if pages <= 0:
            raise ValueError("Ошибка. pages должен быть больше 0")
        self.__pages = pages

    def __str__(self):
        return "Бумажная к" + super().__str__()[1:] + f" Количество страниц {self.pages}."

    def __repr__(self):
        return super().__repr__()[:-1] + f", pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, float):
            raise TypeError("Ошибка. duration должен быть float")
        if duration <= 0:
            raise ValueError("Ошибка. duration должен быть больше 0")
        self.__duration = duration

    def __str__(self):
        # Перегрузка без обращения через super к методу родительского класса
        return f"Аудиокнига {self.name!r}. Автор {self.author!r}. Длительность {round(self.duration, 2)}."

    def __repr__(self):
        return super().__repr__()[:-1] + f", duration={round(self.duration, 2)})"


if __name__ == '__main__':
    # Проверка работоспособности
    book = Book('Азбука', 'Крузенштерн')
    print(book)
    print(repr(book) + '\n')

    paper = PaperBook('У лукоморья', 'Пушкин', 26)
    print(paper)
    print(repr(paper) + '\n')

    audio = AudioBook('Герой нашего времени', 'Лермонтов', 54.97)
    print(audio)
    print(repr(audio))
