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


def test_sample_category_creation(sample_category):
    """Тест создания категории"""
    assert sample_category.name == "Овощи"
    assert sample_category.description == "Овощи для салата"
    assert len(sample_category.products) == 2


def test_empty_category_creation(empty_category):
    """Тест создания пустой категории"""
    assert empty_category.name == "Пустая категория"
    assert empty_category.description == "Категория без товаров"
    assert len(empty_category.products) == 0
