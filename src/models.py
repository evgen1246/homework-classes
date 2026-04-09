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

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для получения списка товаров в виде строки."""
        if not self.__products:
            return "В категории нет товаров"
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(result)

    @property
    def products_list(self) -> List[Product]:
        """Свойство для получения списка товаров (только для чтения)."""
        return self.__products.copy()
