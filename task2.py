# #task1
# class Ball(object):
#     def __init__(self, ball_type="regular"):
#         self.ball_type = ball_type
#
# ball1 = Ball()
# ball2 = Ball("lox")
#
# print(ball1.ball_type)
# print(ball2.ball_type)

# #task2
# import random
# class Ghost(object):
#     def __init__(self):
#         colors = ["white", "yellow", "purple", "red"]
#         self.color = random.choice(colors)
#
# gh1 = Ghost()
# print(gh1.color)

# #task3
# class Human:
#     def __init__(self, name):
#         self.name = name
#
# class Woman(Human):
#     def __init__(self, name):
#         super().__init__(name)
#
# class Man(Human):
#     def __init__(self, name):
#         super().__init__(name)
#
# def God():
#     adam = Man("Adam")
#     eve = Woman("Eve")
#     return [adam, eve]
#
# adam, eve = God()
#
# print(adam.name)
# print(eve.name)

# #task4
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.info= f"{name}s age is {age}"
#
# marik = Person("Marik", 24)
# print(marik.info)

# #task5
# import math
# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#
#     def get_radius(self):
#         return self.radius
#
#     def get_mass(self):
#         return self.mass
#
#     def get_volume(self):
#         volume = (4/3) * math.pi * self.radius**3
#         return round(volume, 5)
#
#     def get_surface_area(self):
#         surf_area = 4 * math.pi * self.radius**2
#         return round(surf_area, 5)
#
#     def get_density(self):
#         return round(self.mass / self.get_volume(), 5)
#
# mysphere = Sphere(2, 40)
# print(mysphere.get_volume())
# print(mysphere.get_mass())
# print(mysphere.get_density())
# print(mysphere.get_radius())
# print(mysphere.get_surface_area())

# #task6
# import re
#
# def class_name_changer(cls, new_name):
#     if not re.match(r'^[A-Z][a-zA-Z0-9]*$', new_name):
#         raise ValueError("Invalid class name. Class names must start with an uppercase letter "
#                          "and contain only alphanumeric characters.")
#
#     cls.__name__ = new_name
#
# class MyClass:
#     pass
#
# class_name_changer(MyClass, "UsefulClass")
import datetime

class Citizen:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def calculate_age(self, current_date):
        birth_year = self.birth_date.year
        current_year = current_date.year
        age = current_year - birth_year
        if (current_date.month, current_date.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

class Client:
    def __init__(self, citizen, bank_account):
        self.citizen = citizen
        self.bank_account = bank_account

    def __str__(self):
        return f"Client: {self.citizen.first_name} {self.citizen.last_name}, Account Number: {self.bank_account.account_number}, Balance: {self.bank_account.balance}"

class VipClient(Client):
    def __init__(self, citizen, bank_account, credit_account_limit, credit_interest_rate):
        super().__init__(citizen, bank_account)
        self.credit_account_limit = credit_account_limit
        self.credit_interest_rate = credit_interest_rate
        self.credit_account_balance = 0
        self.last_credit_date = None

    def apply_for_credit(self, amount, current_date):
        age = self.citizen.calculate_age(current_date)
        max_credit_percentage = self.credit_interest_rate / 100

        if 30 <= age <= 50:
            max_credit_amount = self.bank_account.balance * (self.credit_account_limit / 100)
        else:
            max_credit_amount = self.bank_account.balance * (self.credit_account_limit / 200)

        if 0 < amount <= max_credit_amount:
            self.credit_account_balance += amount
            self.last_credit_date = current_date
            return True
        else:
            return False

    def repay_credit(self, amount):
        if 0 < amount <= self.credit_account_balance:
            self.credit_account_balance -= amount
            return True
        else:
            return False

    def __str__(self):
        return f"VIP Client: {self.citizen.first_name} {self.citizen.last_name}, Account Number: {self.bank_account.account_number}, " \
               f"Balance: {self.bank_account.balance}, Credit Limit: {self.credit_account_limit}, Credit Balance: {self.credit_account_balance}"

# Приклад використання:
citizen1 = Citizen("John", "Doe", datetime.date(1980, 5, 15))
account1 = BankAccount("123456789", 5000)
client1 = Client(citizen1, account1)

vip_citizen1 = Citizen("Jane", "Smith", datetime.date(1975, 8, 10))
vip_account1 = BankAccount("987654321", 10000)
vip_client1 = VipClient(vip_citizen1, vip_account1, 50, 10)

print(client1)
print(vip_client1)

# Додавання коштів на рахунок та виведення балансу
account1.deposit(2000)
vip_account1.deposit(3000)
print(f"Client 1 Balance: {account1.get_balance()}")
print(f"VIP Client 1 Balance: {vip_account1.get_balance()}")

# Зняття грошей з рахунку
account1.withdraw(1000)
vip_account1.withdraw(2000)
print(f"Client 1 Balance after withdrawal: {account1.get_balance()}")
print(f"VIP Client 1 Balance after withdrawal: {vip_account1.get_balance()}")

# Оформлення кредиту та погашення для VIP-клієнта
vip_client1.apply_for_credit(3000, datetime.date(2023, 5, 1))
print(f"VIP Client 1 Credit Balance: {vip_client1.credit_account_balance}")
vip_client1.repay_credit(1500)
print(f"VIP Client 1 Credit Balance after repayment: {vip_client1.credit_account_balance}")
