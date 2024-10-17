# Membuat simple Inheritance dengan method pass
class Animal:
    # Membuat Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Membuat Method
    def sound(self):
        print(f"This {self.name} makes a sound, And {self.name} is {self.age} years old")

    # Membuat Class Turunan / Subclass
class Dog(Animal):
    pass

name = input("Masukkan Nama Anjing Anda : ")
dog = Dog(name, 3)
dog.sound()