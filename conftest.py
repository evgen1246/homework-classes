import pytest

from src.models import Category, LawnGrass, Product, Smartphone


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


@pytest.fixture
def sample_smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def another_smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "128GB, Серый цвет, 100MP камера", 100000.0, 15, 90.5, "S23", 128, "черный"
    )


@pytest.fixture
def sample_lawn_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def another_grass():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
