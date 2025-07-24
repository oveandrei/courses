
'''Simple class example with attribute, method, object creation and usage'''
class Car:
    def __init__(self, brand, year):
        self.brand = brand # attribute
        self.year = year

    def honk(self):     # Method
        return f"{self.brand} goes beep!"

# Object creation
my_car = Car("Toyota", 2020)

print(my_car.brand) # Toyota
print(my_car.honk()) # Toyota goes beep


'''Inheritance Example'''
class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):
    pass

class Dog(Animal): # Inherits from Animal
    def speak(self): # override method  # type: ignore
        return "Woof!"

dog = Dog()
cat = Cat()
print(cat.speak()) # Some sound
print(dog.speak()) # Woof!


'''Encapsulaton Example'''
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # Private attribute only accessible within the class
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount

acc = BankAccount("Alice", 1000)
acc.deposit(200)
print(acc.get_balance()) # 1200
#print(acc.self.__balance) # Raises AttributeError: "BankAccount" has no attribute '__balance'


'''Polymorphism Examples'''
class Lion:
    def speak(self):
        return "Rawrr"

class Cow:
    def speak(self):
        return "Moo"
# Polymorphism allows different classes to be treated as instances of the same class through a common interface
def animal_sound(animal): # Function tht accepts any object with the speak method
    print(animal.speak())

animal_sound(Lion()) # Rawrr
animal_sound(Cow()) # Moo


'''Abstract Class example'''
from abc import ABC, abstractmethod

class Shape(ABC): # Abstract base class
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape): # Inherits from Shape
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self): # Rectangle MUST implement area method
        return self.w * self.h
    
r = Rectangle(10, 5)
print(r.area()) # 50