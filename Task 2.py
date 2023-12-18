# Створіть клас для конвертування температури з Цельсія у Фаренгейт, і навпаки.
# У класі має знаходитися два статичні методи: для конвертування з Цельсія у Фаренгейт і
# для конвертування з Фаренгейта у Цельсій. Також клас має розрахувати кількість підрахунків температури
# та повернути це значення статичним методом.
class TemperatureConverter:

    conversion_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.conversion_count += 1
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.conversion_count += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_conversion_count():
        return TemperatureConverter.conversion_count

celsius_temperature = 20
converted_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} Celsius is equal to {converted_fahrenheit:.2f} Fahrenheit")

fahrenheit_temperature = 68
converted_celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} Fahrenheit is equal to {converted_celsius:.2f} Celsius")

print(f"Count of temperature conversions: {TemperatureConverter.get_conversion_count()}")
