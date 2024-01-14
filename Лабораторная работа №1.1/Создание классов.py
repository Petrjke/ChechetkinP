# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class AssaultRifle:
    def __init__(self, magazine_size: int, rate_of_fire: int, caliber: float):
        """
        Создание и подготовка к работе объекта "Автомат"

        :param magazine_size: Размер магазина автомата
        :param rate_of_fire: Скорострельность автомата
        :param caliber: Калибр автомата

        Примеры:
        >>> rifle = AssaultRifle(30, 600, 5.56)  # инициализация экземпляра класса
        """
        if not isinstance(magazine_size, int):
            raise TypeError("Размер магазина должен быть целым числом")
        if magazine_size <= 0:
            raise ValueError("Размер магазина должен быть положительным числом")
        self.magazine_size = magazine_size

        if not isinstance(rate_of_fire, int):
            raise TypeError("Скорострельность должна быть целым числом")
        if rate_of_fire <= 0:
            raise ValueError("Скорострельность должна быть положительным числом")
        self.rate_of_fire = rate_of_fire

        if not isinstance(caliber, (int, float)):
            raise TypeError("Калибр должен быть числом")
        if caliber <= 0:
            raise ValueError("Калибр должен быть положительным числом")
        self.caliber = caliber

    def is_high_caliber(self) -> bool:
        """
        Функция, которая проверяет, является ли калибр автомата высоким.

        :return: Является ли калибр автомата высоким

        Примеры:
        >>> rifle = AssaultRifle(30, 600, 5.56)
        >>> rifle.is_high_caliber()
        """

        ...

    def increase_rate_of_fire(self, additional_fire_rate: int) -> None:
        """
        Увеличение скорострельности автомата.

        :param additional_fire_rate: Дополнительная скорострельность

        Примеры:
        >>> rifle = AssaultRifle(30, 600, 5.56)
        >>> rifle.increase_rate_of_fire(100)
        """
        if not isinstance(additional_fire_rate, int):
            raise TypeError("Дополнительная скорострельность должна быть целым числом")
        if additional_fire_rate <= 0:
            raise ValueError("Дополнительная скорострельность должна быть положительным числом")


class ComputerMouse:
    def __init__(self, button_count: int, mouse_type: str, resolution: int):
        """
        Создание и подготовка к работе объекта "Компьютерная мышь"

        :param button_count: Количество кнопок мыши
        :param mouse_type: Тип мыши (игровая или офисная)
        :param resolution: Разрешение мыши

        Примеры:
        >>> mouse = ComputerMouse(3, "office", 1200)  # инициализация экземпляра класса
        """
        if not isinstance(button_count, int):
            raise TypeError("Количество кнопок должно быть целым числом")
        if button_count <= 0:
            raise ValueError("Количество кнопок должно быть положительным числом")
        self.button_count = button_count

        if mouse_type.lower() not in ["office", "gaming"]:
            raise ValueError("Тип мыши должен быть 'office' или 'gaming'")
        self.mouse_type = mouse_type.lower()

        if not isinstance(resolution, int):
            raise TypeError("Разрешение мыши должно быть целым числом")
        if resolution <= 0:
            raise ValueError("Разрешение мыши должно быть положительным числом")
        self.resolution = resolution

    def is_gaming_mouse(self) -> bool:
        """
        Функция, которая проверяет, является ли мышь игровой.

        :return: Является ли мышь игровой

        Примеры:
        >>> mouse = ComputerMouse(3, "office", 1200)
        >>> mouse.is_gaming_mouse()
        """

        ...

    def has_high_resolution(self) -> bool:
        """
        Функция, которая проверяет, имеет ли мышь высокое разрешение.

        :return: Имеет ли мышь высокое разрешение

        Примеры:
        >>> mouse = ComputerMouse(3, "office", 1200)
        >>> mouse.has_high_resolution()
        """
        ...

class Person:
    def __init__(self, gender: str, eye_color: str, height: float):
        """
        Создание и подготовка к работе объекта "Человек"

        :param gender: Пол человека
        :param eye_color: Цвет глаз
        :param height: Рост

        Примеры:
        >>> person = Person("male", "blue", 180.0)  # инициализация экземпляра класса
        """
        if gender.lower() not in ["male", "female"]:
            raise ValueError("Пол должен быть 'male' или 'female'")
        self.gender = gender.lower()

        self.eye_color = eye_color

        if not isinstance(height, (int, float)):
            raise TypeError("Рост должен быть числом")
        if height <= 0:
            raise ValueError("Рост должен быть положительным числом")

    def change_eye_color(self, new_color: str) -> None:
        """
        Изменение цвета глаз у человека.

        :param new_color: Новый цвет глаз

        Примеры:
        >>> person = Person("male", "blue", 180.0)
        >>> person.change_eye_color("green")
        """
        ...

    def change_height(self, new_height: float) -> None:
        """
        Изменение роста человека.

        :param new_height: Новый рост

        Примеры:
        >>> person = Person("male", "blue", 180.0)
        >>> person.change_height(185.0)
        """
        if not isinstance(new_height, (int, float)):
            raise TypeError("Новый рост должен быть числом")
        if new_height <= 0:
            raise ValueError("Новый рост должен быть положительным числом")
        ...

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest

