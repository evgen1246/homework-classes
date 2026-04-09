from src.models import Product


def test_product(sample_product):
    """Тест создания товара."""
    assert sample_product.name == "Овощи"
    assert sample_product.description == "Огурцы колючие"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 20


def test_another_product(another_product):
    """Тест создания другого товара."""
    assert another_product.name == "Помидор"
    assert another_product.description == "Помидоры сливовидные"
    assert another_product.price == 80.0
    assert another_product.quantity == 30


def test_product_price_getter(sample_product):
    """Тест геттера цены."""
    assert sample_product.price == 100.0


def test_product_price_setter_valid():
    prod = Product("Продукт", "Описание", 500.0, 10)
    prod.price = 600.0
    assert prod.price == 600.0


def test_product_price_setter_zero(capsys):
    """Тест установки нулевой цены."""
    prod = Product("Продукт", "Описание", 500.0, 10)
    prod.price = 0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_product_price_setter_negative(capsys):
    """Тест установки отрицательной цены."""
    prod = Product("Продукт", "Описание", 500.0, 10)
    prod.price = -100
    assert prod.price == 500.0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_product_new_product_class_method():
    """Тест класс-метода new_product."""
    product_data = {
        "name": "Редиска",
        "description": "Красная редиска",
        "price": 100.0,
        "quantity": 10,
    }
    prod = Product.new_product(product_data)
    assert prod.name == "Редиска"
    assert prod.description == "Красная редиска"
    assert prod.price == 100.0
    assert prod.quantity == 10


def test_product_str_method(sample_product):
    """Тест строкового представления товара."""
    expected = "Овощи, 100.0 руб. Остаток: 20 шт."
    product_str = f"{sample_product.name}, {sample_product.price} руб. Остаток: {sample_product.quantity} шт."
    assert product_str == expected


def test_sample_category_creation(sample_category):
    """Тест создания категории"""
    assert sample_category.name == "Овощи"
    assert sample_category.description == "Овощи для салата"
    assert len(sample_category.products_list) == 2


def test_empty_category_creation(empty_category):
    """Тест создания пустой категории"""
    assert empty_category.name == "Пустая категория"
    assert empty_category.description == "Категория без товаров"
    assert len(empty_category.products_list) == 0
