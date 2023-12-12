class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self.name

    @property
    def author(self) -> str:
        return self.author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            TypeError()
        if value <= 0:
            ValueError('value must be positive')
        self._pages = value


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
    @property
    def duration(self) -> float:
        return self.duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            TypeError()
        if value <= 0:
            ValueError('value must be positive')
        self._duration = value

