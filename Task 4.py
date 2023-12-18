# Створіть клас InformationSystem,
# який має атрибут data - словник, де ключі - це імена користувачів,
# а значення список їх контактів.
# Реалізуйте методи класу для додавання нових користувачів та їх контактів.
class InformationSystem:
    data = {}

    @classmethod
    def add_user(cls, username):
        if username in cls.data:
            print(f"Користувач з ім'ям {username} вже існує.")
        else:
            cls.data[username] = []

    @classmethod
    def add_contact(cls, username, contact):
        if username not in cls.data:
            print(f"Користувача з ім'ям {username} не знайдено.")
        else:
            cls.data[username].append(contact)
            print(f"Контакт {contact} додано для користувача {username}.")

InformationSystem.add_user("Джон")
InformationSystem.add_user("Аліса")

InformationSystem.add_contact("Джон", "Боб")
InformationSystem.add_contact("Джон", "Чарлі")
InformationSystem.add_contact("Аліса", "Девід")

print("Інформаційна система:")
print(InformationSystem.data)