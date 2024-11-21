#Implementasi Polymorph dengan Bangun Datar
class bangundatar: #Abstract Class
    def luas(self): #Abstract Method
        raise NotImplementedError("Method ini wajib diimplementasikan")
    
class persegi(bangundatar): #kelas Turunan 1
    def __init__(self, sisi):
        self.sisi = sisi
    def luas(self):
        print(f"Luas Persegi Adalah     : {self.sisi**2}")
class segitiga(bangundatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def luas(self):
        print(f"Luas Segitiga Adalah    : {(self.alas*self.tinggi)/2}")
class lingkaran(bangundatar):
    def __init__(self, r=0, pi=3.14):
        self.pi = pi
        self.r = r
    def luas(self):
        print(f"Luas Lingkaran Adalah   : {self.pi*self.r**2}")
objek1 = persegi(2)
objek2 = segitiga(2,3)
objek3 = lingkaran(5)
objek1.luas()
objek2.luas()
objek3.luas()