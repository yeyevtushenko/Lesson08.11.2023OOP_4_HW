"""До вже реалізованого класу «Дріб» додайте статичний метод,
який при виклику повертає кількість створених об’єктів класу «Дріб»."""
class Fraction:
    object_count = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.object_count += 1

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    @staticmethod
    def get_object_count():
        return Fraction.object_count

fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

print(f"Count of created objects of the 'Fraction' class: {Fraction.get_object_count()}")