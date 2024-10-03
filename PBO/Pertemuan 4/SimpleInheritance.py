#Membuat Sebuah Super Class
class Animal:
    #Membuat Konstruktor Penampung Atribut
    def __init__(self, name, ras):
        self.name = name
        self.ras = ras
    #Method Suara
    def speaks(self):
        print(f"{self.name} Bisa Bersuara")
# Membuat Class Turunan Dari Superclass
class Cat(Animal):
    def speaksCat(self):
        print(f"Nama {self.name} dengan Ras {self.ras} bersuara Meoow")
#Membuat Class 2 Turunan dari SuperClass
class Dog(Animal):
    def speaksDog(self):
        print(f"Nama {self.name} dari Ras {self.ras} Bersuara Guk Guk")
#Membuat Objek
cat = Cat("Kitty", "Anggora")
cat.speaksCat()
dog = Dog("Puppy", "Pitbull")
dog.speaksDog()