from typing import List, Optional


class Product:
    """Класс для представления товара."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории товаров."""

    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        # Увеличиваем счётчик категорий при создании нового объекта
        Category.category_count += 1

        # Увеличиваем счётчик продуктов при создании нового объекта
        Category.total_products = len(self.products)


