class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers with precision and zero optimization."""
        if a == 0 or b == 0:
            return 0.0  # Explicit zero handling for better performance
        result = a * b
        return round(result, 10)  # Handle floating point precision

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    @staticmethod
    def cube(a: float) -> float:
        """Calculate the cube of a number."""
        # TODO: Will be refactored to use square() after its PR is merged.
        if not isinstance(a, (int, float)):
            raise TypeError("Argument must be a number")
        return float(a) ** 3
