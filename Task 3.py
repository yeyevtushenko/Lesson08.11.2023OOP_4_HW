# Створіть клас для конвертування з метричної системи в англійську, та навпаки.
# Реалізуйте функціональність у вигляді статичних методів.
# Обов’язково реалізуйте конвертування заходів довжини.
class LengthConverter:
    METERS_TO_FEET = 3.28084
    CENTIMETERS_TO_INCHES = 0.393701

    @staticmethod
    def convert_meters_to_feet(meters):
        """
        Convert length from meters to feet.
        """
        return meters * LengthConverter.METERS_TO_FEET

    @staticmethod
    def convert_feet_to_meters(feet):
        return feet / LengthConverter.METERS_TO_FEET

    @staticmethod
    def convert_centimeters_to_inches(centimeters):
        return centimeters * LengthConverter.CENTIMETERS_TO_INCHES

    @staticmethod
    def convert_inches_to_centimeters(inches):
        return inches / LengthConverter.CENTIMETERS_TO_INCHES


meters_length = 5
feet_length = 16.4042
centimeters_length = 10
inches_length = 3.93701

converted_feet = LengthConverter.convert_meters_to_feet(meters_length)
converted_meters = LengthConverter.convert_feet_to_meters(feet_length)
converted_inches = LengthConverter.convert_centimeters_to_inches(centimeters_length)
converted_centimeters = LengthConverter.convert_inches_to_centimeters(inches_length)

print(f"{meters_length} meters is equal to {converted_feet:.2f} feet")
print(f"{feet_length} feet is equal to {converted_meters:.2f} meters")
print(f"{centimeters_length} centimeters is equal to {converted_inches:.2f} inches")
print(f"{inches_length} inches is equal to {converted_centimeters:.2f} centimeters")