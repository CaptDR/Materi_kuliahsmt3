#Membuat Class
class Mobil:

    #Membuat Class Variable
    jumlah_mobil = 0

    #Membuat Constructor
    def __init__(self, ban, merk, cc):

        #Instance Variable
        self.merkban = ban
        self.merkmobil = merk
        self.kapasitas = cc
        Mobil.jumlah_mobil += 1

    #Membuat Method String
    def __str__(self):
        return f"{self.merkban}, {self.merkmobil}, {self.kapasitas}"
    #Membuat Method Baru
    def boreup(self, bore):
        self.kapasitas += bore
        
#Membuat Objek Baru M1
M1 = Mobil("Bridgestone", "Toyota-Kijang", 1500)
print(M1)
print("Jumlah Mobil : ", Mobil.jumlah_mobil)
M1.boreup(500)
print(M1)

#Membuat Objek Baru M2
M2 = Mobil("Pirelli", "Supra", 3000)
print(M2)
print("Jumlah Mobil : ", Mobil.jumlah_mobil)