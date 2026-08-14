# class Animal:
#     def make_sound(self)
#         print("звук")
#
#
# class Dog(Animal):
#     def sound(self):
#         print("OUW OUW")
#
#
# class Cat(Animal):
#     def makesound(self):
#         print("meeooooww")

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        print("sound")

# animal1 = Animal()

class Dog(Animal):
    def makesound(self):
        print("Ouw Ouw")

