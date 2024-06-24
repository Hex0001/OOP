from typing import Optional


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


class Library:
    def __init__(self, books: Optional[list[Book]] = None):
        """
        Инициализирует объект "Библиотека"

        :param books: Список книг, состоящий из объектов класса Book
        """
        if books is None:
            books = []
        if not isinstance(books, list):
            raise TypeError("Ошибка. books должны быть списком")
        for book in books:
            if not isinstance(book, Book):
                raise TypeError("Ошибка. Элементы списка должны быть объектами класса Book")
        self.books = books.copy()

    def get_next_book_id(self) -> int:
        """
        Метод находит максимальный id_ книги в списке, который хранится в атрибуте экземпляра класса и возвращает
        значение на единицу больше

        :return: Идентификатор, следующий по порядку после максимального
        """
        if not self.books:
            return 1
        return max(self.books, key=lambda book: book.id_).id_ + 1

    def get_index_by_book_id(self, id_: int) -> int:
        """
        Метод возвращает индекс книги с требуемым id_ в списке, который хранится в атрибуте экземпляра класса

        :param id_: Идентификатор книги
        :return: Индекс элемента с требуемым id_ в списке books
        """
        for index, book in enumerate(self.books):
            if id_ == book.id_:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки
    #
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
