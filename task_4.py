if __name__ == "__main__":
    class Animal:
        """Базовый класс, представляющий животных."""

        def __init__(self, species: str, preparation: str):
            self._species = species  # Species of the animal
            self._preparation = preparation  # How the animal preparation for winter

        def preparation_for_winter(self) -> str:
            """
            То, как животное готовится к зиме.
            Returns:
            str: Способ подготовки.
            """
            return self._preparation

        def get_species(self) -> str:
            """
            Получить вид животного.
            Returns:
            str: Вид животного.
            """
            return self._species

        def __str__(self) -> str:
            return f"Животное {self._species}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}({self._species}, {self._preparation})"


    class Bear(Animal):
        """Производный класс, представляющий медведей."""

        def __init__(self, species: str, preparation: str, kind: str):
            super().__init__(species, preparation)
            self._kind = kind  # Kind of the bear

        def preparation_for_winter(self) -> str:
            return "Ложится в спячку"


    def __str__(self) -> str:
        return f"Медведь {self._kind}"


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._species}, {self._preparation}, {self._kind})"


class Rabbit(Animal):
    """Производный класс, представляющий зайцев."""

    def __init__(self, species: str, preparation: str, color: str):
        super().__init__(species, preparation)
        self._color = color  # Color of the rabbit

    def get_color(self) -> str:
        """
            Получить окрас зайца.
            Returns:
            str: Окрас зайца.
        """
        return self._color

    def preparation_for_winter(self) -> str:
        return "Меняет шубку."

    def __str__(self) -> str:
        return f"Заец окраса {self._color}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._species}, {self._preparation}, {self._color})"

    pass


if __name__ == "__main__":
    # Write your solution here
    pass
