from typing import Union

import doctest


class GameCharacter:
    def __init__(self, name: str,  max_health: Union[int, float], health: Union[int, float], armor: Union[int, float]):
        """
        Инициализация объекта "Игровой персонаж"

        :param name: Имя игрового персонажа
        :param max_health: Максимальное здоровье
        :param health: Текущее здоровье
        :param armor: Количество брони

        Примеры:
        >>> man = GameCharacter('Шарик', 100, 80, 10)

        >>> man = GameCharacter('Матроскин', 10, 80, 30)
        Traceback (most recent call last):
        ValueError: Ошибка. health должен быть больше либо равен нулю и меньше max_health
        >>> man = GameCharacter(21, 1, 0, 30)
        Traceback (most recent call last):
        TypeError: Ошибка. name должен быть типа str
        """

        self.name = None
        self.max_health = None
        self.health = None
        self.armor = None

        self.init_name(name)
        self.init_max_health(max_health)
        self.init_health(health)
        self.init_armor(armor)

    def init_name(self, name: str) -> None:
        """
        Метод, который проверяет переданное имя игрового персонажа. Если значение подходящее, присваивает новое значение
        атрибуту объекта

        :param name: Имя игрового персонажа
        :return: None

        Примеры:
        >>> man = GameCharacter('Шарик', 100, 80, 10)
        >>> print(man.name)
        Шарик
        >>> man.init_name('Вася')
        >>> print(man.name)
        Вася
        """
        if not isinstance(name, str):
            raise TypeError("Ошибка. name должен быть типа str")
        self.name = name

    def init_max_health(self, max_health: Union[int, float]) -> None:
        """
        Метод, который проверяет переданное максимальное здоровье. Если значение подходящее, присваивает новое значение
        атрибуту объекта

        :param max_health: Максимальное здоровье
        :return: None

        Примеры:
        >>> man = GameCharacter('Шарик', 100, 80, 10)
        >>> print(man.max_health)
        100
        >>> man.init_max_health(180)
        >>> print(man.max_health)
        180
        """
        if not isinstance(max_health, (int, float)):
            raise TypeError("Ошибка. max_health должен быть типа int или float")
        if max_health < 0:  # Оставил ноль на случай создания условного служебного персонажа с нулевым здоровьем
            raise ValueError("Ошибка. max_health должен быть больше либо равен нулю")
        self.max_health = max_health

    def init_health(self, health: Union[int, float]) -> None:
        """
        Метод, который проверяет переданное текущее здоровье. Если значение подходящее, присваивает новое значение
        атрибуту объекта

        :param health: Текущее здоровье
        :return: None

        Примеры:
        >>> man = GameCharacter('Шарик', 100, 80, 10)
        >>> print(man.health)
        80
        >>> man.init_health(30)
        >>> print(man.health)
        30
        """
        if not isinstance(health, (int, float)):
            raise TypeError("Ошибка. health должен быть типа int или float")
        if health < 0 or health > self.max_health:
            raise ValueError("Ошибка. health должен быть больше либо равен нулю и меньше max_health")
        self.health = health

    def init_armor(self, armor: Union[int, float]) -> None:
        """
        Метод, который проверяет переданное количество брони. Если значение подходящее, присваивает новое значение
        атрибуту объекта

        :param armor: Количество брони
        :return: None

        Примеры:
        >>> man = GameCharacter('Шарик', 100, 80, 10)
        >>> print(man.armor)
        10
        >>> man.init_armor(37)
        >>> print(man.armor)
        37
        """
        if not isinstance(armor, (int, float)):
            raise TypeError("Ошибка. armor должен быть типа int или float")
        if armor < 0:
            raise ValueError("Ошибка. armor должен быть больше либо равен нулю")
        self.armor = armor

    def increase_health(self, health_increment: Union[int, float]) -> None:
        """
        Метод увеличивает текущее здоровье на указанную величину.

        :param health_increment: Количество здоровья, на которое необходимо увеличить текущее здоровье
        :return: None

        Примеры:
        >>> man = GameCharacter('Шарик', 100, 80, 10)
        >>> print(man.health)
        80
        >>> man.increase_health(7)
        >>> print(man.health)
        87
        >>> man.increase_health(30)
        >>> print(man.health)
        100
        """
        if not isinstance(health_increment, (int, float)):
            raise TypeError("Ошибка. Значение увеличения здоровья health_increment должно быть int или float")
        if health_increment <= 0:
            raise ValueError("Ошибка. Значение увеличения здоровья health_increment должно быть строго положительным")

        self.health = self.health + health_increment if self.health + health_increment < self.max_health \
            else self.max_health

    def reduce_health(self, health_damage: Union[int, float]) -> None:
        """
        Метод уменьшает текущее здоровье на указанную величину. На вход подаётся итоговый показатель уменьшения здоровья
        (с учётом ранее рассчитанной брони и урона).

        :param health_damage: Количество здоровья, на которое необходимо уменьшить текущее здоровье
        :return: None

        Примеры:
        >>> man = GameCharacter('Шарик', 100, 80, 10)
        >>> print(man.health)
        80
        >>> man.reduce_health(7.2)
        >>> print(man.health)
        72.8
        >>> man.reduce_health(90)
        >>> print(man.health)
        0
        """
        if not isinstance(health_damage, (int, float)):
            raise TypeError("Ошибка. Значение полученного урона health_damage должно быть int или float")
        if health_damage <= 0:
            raise ValueError("Ошибка. Значение полученного урона health_damage должно быть строго положительным")

        self.health = self.health - health_damage if 0 < self.health - health_damage else 0

    def take_damage(self, enemy_damage: Union[int, float]) -> None:
        """
        Метод уменьшает здоровье в зависимости от полученного урона и текущего показателя брони.

        :param enemy_damage: Полученный урон
        :return: None

        Примеры:
        >>> man = GameCharacter('Шарик', 100, 80, 10)
        >>> print(man.health)
        80
        >>> man.take_damage(10)
        >>> print(man.health)
        73.7
        >>> man.take_damage(15)
        >>> print(man.health)
        64.25
        >>> man.take_damage(-15)
        Traceback (most recent call last):
        ValueError: Ошибка. Значение урона enemy_damage должно быть строго положительным
        """
        if not isinstance(enemy_damage, (int, float)):
            raise TypeError("Ошибка. Значение урона enemy_damage должно быть int или float")
        if enemy_damage <= 0:
            raise ValueError("Ошибка. Значение урона enemy_damage должно быть строго положительным")
        reduction = round((self.armor * 0.06) / (1 + self.armor * 0.06), 2)  # Снижение урона в процентах в зависимости
        # от брони, формула с какого-то игрового форума по варкрафту
        health_damage = enemy_damage - enemy_damage * reduction
        self.reduce_health(health_damage)


class Boot:
    boots_database = {'кроссовки', 'кеды', 'туфли'}
    color_database = {'чёрный', 'синий', 'красный', 'фиолетовый'}  # Скорее всего все базы обычно пишутся за пределами
    # класса, сделано ради эксперимента

    def __init__(self, boot_type: str, size: Union[int, float], color: str):
        """
        Инициализация объекта "Ботинок"

        :param boot_type: Тип ботинка
        :param size: Размер ботинка
        :param color: Цвет ботинка

        Примеры:
        >>> boot = Boot('кроссовки', 36, 'фиолетовый')

        >>> boot = Boot('мокасины', 60, 'красный')
        Traceback (most recent call last):
        ValueError: Ошибка. Типа обуви 'мокасины' нет в базе данных (boots_database - атрибут класса)
        >>> boot = Boot('кроссовки', -4, 'синий')
        Traceback (most recent call last):
        ValueError: Ошибка. Размер ботинка size должен быть в пределах от 16 до 60
        >>> boot = Boot('кроссовки', 36, 1)
        Traceback (most recent call last):
        TypeError: Ошибка. color должен быть str
        """
        if not isinstance(boot_type, str):
            raise TypeError("Ошибка. Тип обуви boot_type должен быть str")
        if boot_type not in Boot.boots_database:
            raise ValueError(f"Ошибка. Типа обуви '{boot_type}' нет в базе данных (boots_database - атрибут класса)")
        self.boot_type = boot_type

        if not isinstance(size, (int, float)):
            raise TypeError("Ошибка. Размер ботинка size должен быть int или float")
        if not (16 <= size <= 60):
            raise ValueError("Ошибка. Размер ботинка size должен быть в пределах от 16 до 60")  # Допустим, что
            # продаются только такие размеры
        self.size = size

        if not isinstance(color, str):
            raise TypeError("Ошибка. color должен быть str")
        if color not in Boot.color_database:
            raise ValueError(f"Ошибка. Цвета  '{color}' нет в базе данных (color_database - атрибут класса)")
        self.color = color

    def delta_size(self, size: Union[int, float]) -> None:
        """
        Метод изменяет размер ботинка на указанную величину (положительную или отрицательную).

        :param size: Значение размера ботинка, на которое необходимо изменить текущий размер
        :return: None

        Примеры:
        >>> boot = Boot('кроссовки', 36, 'фиолетовый')
        >>> boot.delta_size(5)
        >>> print(boot.size)
        41
        >>> boot.delta_size(-7)
        >>> print(boot.size)
        34
        >>> boot.delta_size(-100)
        >>> print(boot.size)
        16
        """
        if not isinstance(size, (int, float)):
            raise TypeError("Ошибка. Размер ботинка size должен быть int или float")
        if size >= 0:
            self.size = self.size + size if self.size + size <= 60 else 60
        else:
            self.size = self.size + size if 16 <= self.size + size else 16

    @classmethod
    def add_boot_type(cls, boot_type: str) -> None:
        """
        Классовый метод, добавляет в базу данных boots_database новый тип ботинка

        :param boot_type: Добавляемый в базу тип ботинка
        :return: None

        Примеры:
        >>> boot = Boot('мокасины', 60, 'красный')
        Traceback (most recent call last):
        ValueError: Ошибка. Типа обуви 'мокасины' нет в базе данных (boots_database - атрибут класса)
        >>> Boot.add_boot_type('мокасины')
        >>> boot = Boot('мокасины', 60, 'красный')

        """
        if not isinstance(boot_type, str):
            raise TypeError("Ошибка. boot_type должен быть str")
        cls.boots_database.add(boot_type)

    @classmethod
    def remove_boot_type(cls, boot_type: str) -> None:
        """
        Классовый метод, удаляет из базы данных boots_database тип ботинка

        :param boot_type: Удаляемый тип ботинка
        :return: None

        Примеры:
        >>> boot = Boot('туфли', 44, 'фиолетовый')

        >>> Boot.remove_boot_type('ботфорты')
        Traceback (most recent call last):
        ValueError: Ошибка удаления. Типа обуви 'ботфорты' нет в базе данных (boots_database - атрибут класса)
        >>> Boot.remove_boot_type('туфли')
        >>> boot = Boot('туфли', 44, 'фиолетовый')
        Traceback (most recent call last):
        ValueError: Ошибка. Типа обуви 'туфли' нет в базе данных (boots_database - атрибут класса)
        """
        if not isinstance(boot_type, str):
            raise TypeError("Ошибка. boot_type должен быть str")
        if boot_type not in cls.boots_database:
            raise ValueError(f"Ошибка удаления. Типа обуви '{boot_type}' нет в базе данных "
                             f"(boots_database - атрибут класса)")
        cls.boots_database.remove(boot_type)


class Guitar:
    def __init__(self, guitar_type: str, strings_count: int, is_electric: bool):
        """
        Инициализация объекта "Гитара"

        :param guitar_type: Тип гитары
        :param strings_count: Количество струн
        :param is_electric: Показывает, электрическая ли гитара. True если гитара электрическая, False если акустическая

        Примеры:
        >>> guitar = Guitar('балалайка', 3, True)

        >>> guitar = Guitar(1, 2, True)
        Traceback (most recent call last):
        TypeError: Ошибка. Тип гитары guitar_type должен быть str
        >>> guitar = Guitar('балалайка', 3, 13)
        Traceback (most recent call last):
        TypeError: Ошибка. is_electric должен быть типа bool
        >>> guitar = Guitar('балалайка', -3, True)
        Traceback (most recent call last):
        ValueError: Ошибка. Количество струн strings_count должен быть больше либо равен нулю
        """
        if not isinstance(guitar_type, str):
            raise TypeError("Ошибка. Тип гитары guitar_type должен быть str")
        self.guitar_type = guitar_type

        if not isinstance(strings_count, int):
            raise TypeError("Ошибка. Количество струн strings_count должен быть int")
        if strings_count < 0:
            raise ValueError("Ошибка. Количество струн strings_count должен быть больше либо равен нулю")
        self.strings_count = strings_count

        if not isinstance(is_electric, bool):
            raise TypeError("Ошибка. is_electric должен быть типа bool")
        self.is_electric = is_electric

    def change_electric(self) -> None:
        """
        Метод, изменяющий показатель электричности/акустичности гитары на противоположный

        :return: None

        Примеры:
        >>> guitar = Guitar('балалайка', 3, True)
        >>> print(guitar.is_electric)
        True
        >>> guitar.change_electric()
        >>> print(guitar.is_electric)
        False
        >>> guitar.change_electric()
        >>> print(guitar.is_electric)
        True
        """
        self.is_electric = not self.is_electric

    def add_strings(self, strings: int) -> None:
        """
        Метод, добавляющий указанное количество струн

        :param strings: Количество струн для добавления
        :return: None

        Примеры:
        >>> guitar = Guitar('советская гитара', 6, False)
        >>> print(guitar.strings_count)
        6
        >>> guitar.add_strings(4)
        >>> print(guitar.strings_count)
        10
        >>> guitar.add_strings('пять')
        Traceback (most recent call last):
        TypeError: Ошибка. Добавляемые струны strings должны быть типа int
        """
        if not isinstance(strings, int):
            raise TypeError("Ошибка. Добавляемые струны strings должны быть типа int")
        if strings <= 0:
            raise ValueError("Ошибка. Добавляемое количество струн strings должно быть строго положительным")
        self.strings_count += strings

    def remove_strings(self, strings: int) -> None:
        """
        Метод, удаляющий указанное количество струн

        :param strings: Количество струн для удаления
        :return: None

        Примеры:
        >>> guitar = Guitar('советская гитара', 6, False)
        >>> print(guitar.strings_count)
        6
        >>> guitar.remove_strings(4)
        >>> print(guitar.strings_count)
        2
        >>> guitar.remove_strings(1.5321)
        Traceback (most recent call last):
        TypeError: Ошибка. Удаляемые струны strings должны быть типа int
        >>> guitar.remove_strings(-3)
        Traceback (most recent call last):
        ValueError: Ошибка. Удаляемое количество струн strings должно быть строго положительным
        >>> guitar.remove_strings(100)
        >>> print(guitar.strings_count)
        0
        """
        if not isinstance(strings, int):
            raise TypeError("Ошибка. Удаляемые струны strings должны быть типа int")
        if strings <= 0:
            raise ValueError("Ошибка. Удаляемое количество струн strings должно быть строго положительным")
        self.strings_count = self.strings_count - strings if 0 <= self.strings_count - strings else 0


if __name__ == "__main__":
    doctest.testmod()
