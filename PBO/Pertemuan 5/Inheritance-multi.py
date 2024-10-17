# Membuat SuperClass Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        pass

# Membuat Subclass Dog yang mewarisi dari Animal
class Dog(Animal):
    def __init__(self, name, age, ras):
        # Inisiasi variable name dan age dari superclass
        super().__init__(name, age)
        self.ras =  ras
    # Method untuk kelas Dog
    def speaksDog(self):
        print(f"Dog {self.name} from ras {self.ras} is {self.age} years old and it's barking")

# Membuat Kelas Turunan dari Dog
class Cat(Dog):
    def __init__(self, name, age, ras, color):
        super().__init__(name, age, ras)
        self.color = color
    def speaksCat(self):
        print(f"Cat {self.name} from ras {self.ras} is {self.age} years old and it's meowing")

dog1 = Dog("Chester", 3, "Siberian Husky")
dog1.speaksDog()
cat1 = Cat("Labubu", 2, "Bengal", "Brown")
cat1.speaksCat()
