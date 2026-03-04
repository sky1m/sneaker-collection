import pytest
from Part_1.Sneaker import Sneaker

def test_sneaker_init():
    """Test the initialization of the Sneaker class."""
    brand = "Nike"
    model = "Air Jordan 1"
    colorway = "Black/Red"
    release_year = 1985
    size = 9.0
    condition = "new"

    sneaker = Sneaker(brand, model, colorway, release_year, size, condition)

    assert sneaker.brand == brand
    assert sneaker.model == model
    assert sneaker.colorway == colorway
    assert sneaker.release_year == release_year
    assert sneaker.size == size
    assert sneaker.condition == condition

def test_sneaker_str():
    """Test the string representation of the Sneaker class."""
    sneaker = Sneaker("Adidas", "Ultraboost", "White", 2020, 10.5, "used")
    expected_str = "Adidas Ultraboost - White, Size: 10.5, Released in 2020, Condition: used"
    assert str(sneaker) == expected_str

def test_sneaker_init_types():
    """Test the Sneaker class with different but valid types."""
    # Although the docstring says release_year is int and size is float,
    # Python doesn't enforce this. Let's see if it handles them.
    sneaker = Sneaker("Vans", "Old Skool", "Black", "2010", 8, "new")
    assert sneaker.release_year == "2010"
    assert sneaker.size == 8
    expected_str = "Vans Old Skool - Black, Size: 8, Released in 2010, Condition: new"
    assert str(sneaker) == expected_str
