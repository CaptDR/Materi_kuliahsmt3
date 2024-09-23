#Membuat Program Paradigma OOP
class Luas:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    def luas_persegipanjang(self):
        return self.panjang * self.lebar
    
cek_luas = Luas(10,10)
print (f"Luas Persegi adalah {cek_luas.luas_persegipanjang()}")