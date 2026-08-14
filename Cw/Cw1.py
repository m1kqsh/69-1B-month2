class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        print("Животное издает звук")


class Dog(Animal):
    def make_sound(self):
        print("Гав-гав!")


class Cat(Animal):
    def make_sound(self):
        print("Мяу!")


dog = Dog("Buddy", 3)
kitty = Cat("Kitty", 1)

dog.make_sound()
kitty.make_sound()

print(dog.get_name())
print(dog.get_age())

print(kitty.get_name())
print(kitty.get_age())

dog.set_name("Rex")
dog.set_age(4)

kitty.set_name("Murka")
kitty.set_age(2)

print(dog.get_name())
print(dog.get_age())

print(kitty.get_name())
print(kitty.get_age())