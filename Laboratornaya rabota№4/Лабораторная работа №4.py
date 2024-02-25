if __name__ == "__main__":
    class Shape:
        """Базовый класс для геометрических фигур."""

        def __init__(self, color: str):
            """Инициализация фигуры с указанием цвета."""
            self._color = color

        def _calculate_area(self) -> float:
            """Закрытый метод для вычисления площади фигуры."""
            pass

        def _calculate_perimeter(self) -> float:
            """Закрытый метод для вычисления периметра фигуры."""
            pass

        def get_color(self) -> str:
            """Получить цвет фигуры."""
            return self._color

        def area(self) -> float:
            """Публичный метод для вычисления площади фигуры."""
            return self._calculate_area()

        def perimeter(self) -> float:
            """Публичный метод для вычисления периметра фигуры."""
            return self._calculate_perimeter()

        def __str__(self) -> str:
            """Строковое представление фигуры."""
            return f"Фигура цвета {self._color}"

        def __repr__(self) -> str:
            """Представление фигуры."""
            return f"{self.__class__.__name__}(цвет={self._color})"


    class Circle(Shape):
        """Дочерний класс для кругов."""

        def __init__(self, color: str, radius: float):
            """Инициализация круга с указанием цвета и радиуса."""
            super().__init__(color)
            self._radius = radius

        def _calculate_area(self) -> float:
            """Вычисление площади круга."""
            return 3.14 * self._radius ** 2

        def _calculate_perimeter(self) -> float:
            """Вычисление длины окружности."""
            return 2 * 3.14 * self._radius

        # Перегрузка метода для обоснования: круг представляется в более читаемом виде.
        def __str__(self) -> str:
            """Строковое представление круга."""
            return f"Круг с радиусом {self._radius} и цветом {self.get_color()}"


    class Rectangle(Shape):
        """Дочерний класс для прямоугольников."""

        def __init__(self, color: str, width: float, height: float):
            """Инициализация прямоугольника с указанием цвета, ширины и высоты."""
            super().__init__(color)
            self._width = width
            self._height = height

        def _calculate_area(self) -> float:
            """Вычисление площади прямоугольника."""
            return self._width * self._height

        def _calculate_perimeter(self) -> float:
            """Вычисление периметра прямоугольника."""
            return 2 * (self._width + self._height)

        # Перегрузка метода для обоснования: прямоугольник представляется в более читаемом виде.
        def __str__(self) -> str:
            """Строковое представление прямоугольника."""
            return f"Прямоугольник со сторонами {self._width}x{self._height} и цветом {self.get_color()}"

    pass
