import pytest
from src.calculator import Calculator


def test_add():
    assert Calculator.add(1, 2) == 3
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(0, 0) == 0


def test_subtract():
    assert Calculator.subtract(3, 2) == 1
    assert Calculator.subtract(1, 1) == 0
    assert Calculator.subtract(0, 5) == -5


def test_multiply_enhanced_functionality():
    """Test enhanced multiply function with zero optimization and precision."""

    # Test zero optimization
    assert Calculator.multiply(0, 5) == 0.0
    assert Calculator.multiply(7, 0) == 0.0
    assert Calculator.multiply(0, 0) == 0.0

    # Test floating point precision handling
    result = Calculator.multiply(0.1, 3)
    assert result == 0.3  # Should be clean 0.3, not 0.30000000000000004

    # Test precision with more complex cases
    assert Calculator.multiply(0.2, 0.2) == 0.04
    assert Calculator.multiply(7, 0.1) == 0.7

    # Test normal integers still work
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(-2, 3) == -6


def test_divide():
    assert Calculator.divide(6, 2) == 3
    assert Calculator.divide(5, 2) == 2.5
    assert Calculator.divide(0, 5) == 0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(5, 0)
