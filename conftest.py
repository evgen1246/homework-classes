import pytest

from src.models import Category, Product


@pytest.fixture
def sample_product():
    return Product("Овощи", "Огурцы колючие", 100.0, 20)


@pytest.fixture
def another_product():
    return Product("Помидор", "Помидоры сливовидные", 80.0, 30)


@pytest.fixture
def sample_category(sample_product, another_product):
    """Фикстура: создаёт категорию с двумя товарами."""
    return Category(
        name="Овощи",
        description="Овощи для салата",
        products=[sample_product, another_product],
    )


@pytest.fixture
def empty_category():
    """Фикстура: создаёт пустую категорию."""
    return Category(name="Пустая категория", description="Категория без товаров")


@pytest.fixture
def reset_counters():
    """Фикстура: сбрасывает счётчики категорий перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0
    yield
