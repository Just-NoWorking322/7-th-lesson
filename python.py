# class User:
#     def study(self):
#         print("учится")

# class Student(User):
#     pass

# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         print("Гав-гав")

# class Cat(Animal):
#     def speak(self):
#         print("Мяу-мяу")

# class Cow(Animal):
#     def speak(self):
#         print("Му-му")

# class Cafe:
#     def __init__(self, name):
#         self.name = name

#     def order(self, dish):
#         print(f"Вы заказали {dish} в кафе {self.name}")

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model} завелась")

    def stop_engine(self):
        print(f"{self.make} {self.model} заглохла")