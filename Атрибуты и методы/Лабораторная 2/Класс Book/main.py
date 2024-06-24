BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализирует объект "Книга"

        :param id_: Идентификатор книги
        :param name: Наименование книги
        :param pages: Количество страниц
        """
        if not isinstance(id_, int):
            raise TypeError("Ошибка. Идентификатор книги должен быть целым")
        if id_ < 0:
            raise ValueError("Ошибка. Идентификатор книги должен быть больше 0")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Ошибка. Имя должно быть строковым значением")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Ошибка. Количество страниц должно быть целым числом")
        if pages < 0:
            raise ValueError("Ошибка. Количество страниц должно быть больше 0")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id_={self.id_}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
