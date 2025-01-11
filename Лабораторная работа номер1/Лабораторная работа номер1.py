import doctest

class Car:
    def __init__(self, brand: str, year: int):
        if year < 1886:
            raise ValueError("Год выпуска автомобиля не может быть раньше 1886 года.")
        self.brand = brand
        self.year = year

    def start_engine(self) -> None:
        """
        >>> car = Car("Tesla", 2020)
        >>> car.start_engine()
        """
        ...

    def drive(self, distance: float) -> None:
        """
        >>> car = Car("Toyota", 2015)
        >>> car.drive(50)
        """
        ...


class Smartphone:
    def __init__(self, model: str, storage: int):
        if storage < 1:
            raise ValueError("Объем памяти смартфона должен быть не меньше 1 ГБ.")
        self.model = model
        self.storage = storage

    def make_call(self, number: str) -> None:
        """
        >>> phone = Smartphone("iPhone", 128)
        >>> phone.make_call("+1234567890")
        """
        ...

    def install_app(self, app_name: str) -> None:
        """
        >>> phone = Smartphone("Samsung", 64)
        >>> phone.install_app("WhatsApp")
        """
        ...


class Book:
    def __init__(self, title: str, pages: int):
        if pages <= 0:
            raise ValueError("Книга должна содержать хотя бы одну страницу.")
        self.title = title
        self.pages = pages

    def read(self, pages: int) -> None:
        """
        >>> book = Book("War and Peace", 1225)
        >>> book.read(100)
        """
        ...

    def bookmark(self, page: int) -> None:
        """
        >>> book = Book("1984", 328)
        >>> book.bookmark(150)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
