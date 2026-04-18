from typing import Any, Dict, List, Optional


class Product:
    """Класс для представления товара."""

    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Строковое представление товара."""
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Возвращает общую стоимость: цена_1 * количество_1 + цена_2 * количество_2"""
        total_cost = (self.price * self.quantity) + (other.price * other.quantity)
        return total_cost

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

    def __str__(self) -> str:
        """ ""Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

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

    def __init__(self, name: str, description: str, efficiency: str, model: str, memory:int, color:str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color



class LawnGrass(Product):
    """Класс для представления газонной травы(наследник Product)."""

    def __init__(self, name: str, description: str, country: str, germination_period: int, color: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price,quantity)
        self.country = country
        self.germination_period= germination_period
        self.color = color
