from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class PrintMixin:
    """Миксин для автоматического логирования создания объектов."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Базовый __init__, который ничего не делает, но принимает аргументы."""
        super().__init__()

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление продукта."""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Геттер для получения цены."""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        """Сеттер для установки цены."""
        pass

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Сложение продуктов (общая стоимость)."""
        pass

    @property
    @abstractmethod
    def quantity(self) -> int:
        """Геттер для получения количества."""
        pass

    @quantity.setter
    @abstractmethod
    def quantity(self, new_quantity: int) -> None:
        """Сеттер для установки количества."""
        pass


class Product(PrintMixin, BaseProduct):
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = price
        self.__quantity = quantity
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        """Строковое представление товара."""
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "BaseProduct") -> float:
        """Возвращает общую стоимость: цена_1 * количество_1 + цена_2 * количество_2"""
        if not isinstance(other, BaseProduct):
            raise TypeError(f"Нельзя сложить Product и {type(other).__name__}")

        if type(self) is not type(other):
            raise TypeError(
                f"Нельзя складывать товары разных классов: " f"{type(self).__name__} и {type(other).__name__}"
            )

        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]) -> "Product":
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def quantity(self) -> int:
        """Геттер для получения количества."""
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        """Сеттер для установки количества с проверкой."""
        if new_quantity < 0:
            print("Количество не может быть отрицательным")
        else:
            self.__quantity = new_quantity


class Category:
    """Класс для представления категории товаров."""

    name: str
    description: str
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        # Увеличиваем счётчик категорий при создании нового объекта
        Category.category_count += 1

        # Увеличиваем счётчик продуктов при создании нового объекта
        Category.product_count += len(self.__products)

    def get_average_price(self) -> float:
        if not self.__products:
            return 0

        try:
            total_price = sum(product.price for product in self.__products)
            count = len(self.__products)
            average_price = total_price / count
            return average_price
        except ZeroDivisionError:
            return 0

    def __str__(self) -> str:
        """ ""Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавить товар в категорию."""
        if isinstance(product, BaseProduct):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        """Геттер для получения списка товаров в виде строки."""
        if not self.__products:
            return "В категории нет товаров"
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self) -> List[Product]:
        """Свойство для получения списка товаров (только для чтения)."""
        return self.__products.copy()


class Smartphone(Product):
    """Класс для представления смартфона (наследник Product)."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы(наследник Product)."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
