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
    capsys.readouterr()
    prod.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert prod.price == 500.0


def test_product_price_setter_negative(capsys):
    """Тест установки отрицательной цены."""
    prod = Product("Продукт", "Описание", 500.0, 10)
    capsys.readouterr()
    prod.price = -100
    assert prod.price == 500.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


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


def test_product_str(sample_product):
    """Тест строкового представления товара."""
    expected = "Овощи, 100 руб. Остаток: 20 шт."
    assert str(sample_product) == expected


def test_product_add(sample_product, another_product):
    """Тест сложения двух товаров."""
    # a = Product("Товар A", "Описание A", 100, 10)
    # b = Product("Товар B", "Описание B", 200, 2)

    result = sample_product + another_product
    expected = 100 * 20 + 80 * 30  # 2000 + 2400 = 4400

    assert result == expected
    assert isinstance(result, float)


def test_smartphone_init(sample_smartphone):
    assert sample_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert sample_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert sample_smartphone.price == 180000.0
    assert sample_smartphone.quantity == 5
    assert sample_smartphone.efficiency == 95.5
    assert sample_smartphone.model == "S23 Ultra"
    assert sample_smartphone.memory == 256
    assert sample_smartphone.color == "Серый"


def test_smartphone_inheritance(sample_smartphone):
    """Тест наследования от Product."""
    assert isinstance(sample_smartphone, Product)
    assert hasattr(sample_smartphone, "price")
    assert hasattr(sample_smartphone, "quantity")


def test_smartphone_price_setter(sample_smartphone):
    """Тест установки цены смартфона."""
    sample_smartphone.price = 171000.0
    assert sample_smartphone.price == 171000.0


def test_smartphone_add_same_class(sample_smartphone, another_smartphone):
    """Тест сложения двух смартфонов."""
    result = sample_smartphone + another_smartphone
    expected = (180000 * 5) + (100000 * 15)
    assert result == expected


def test_lawn_grass_init(sample_lawn_grass):
    assert sample_lawn_grass.name == "Газонная трава"
    assert sample_lawn_grass.description == "Элитная трава для газона"
    assert sample_lawn_grass.price == 500.0
    assert sample_lawn_grass.quantity == 20
    assert sample_lawn_grass.country == "Россия"
    assert sample_lawn_grass.germination_period == "7 дней"
    assert sample_lawn_grass.color == "Зеленый"


def test_lawn_grass_inheritance(sample_lawn_grass):
    """Тест наследования от Product."""
    assert isinstance(sample_lawn_grass, Product)
    assert hasattr(sample_lawn_grass, "price")
    assert hasattr(sample_lawn_grass, "quantity")


def test_lawn_grass_price_setter(sample_lawn_grass):
    """Тест установки цены."""
    sample_lawn_grass.price = 600.0
    assert sample_lawn_grass.price == 600.0


def test_lawn_grass_add(sample_lawn_grass, another_grass):
    """Тест сложения."""
    result = sample_lawn_grass + another_grass
    expected = (500 * 20) + (450 * 15)
    assert result == expected


def test_print_mixin_output(capsys):
    """Тест: при создании продукта PrintMixin выводит repr в консоль."""
    Product("Тест", "Описание", 100.0, 10)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Product(Тест, Описание, 100.0, 10)"


def test_print_mixin_repr_format(sample_product):
    """Тест: формат __repr__ соответствует ожидаемому."""
    expected = "Product(Овощи, Огурцы колючие, 100.0, 20)"
    assert repr(sample_product) == expected
