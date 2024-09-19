class Buku:
    jumlah_buku = 0
    def __init__(self, judul, penulis, tahuntb):
        self.judulbuku = judul
        self.penulisbuku = penulis
        self.tahun = tahuntb
        Buku.jumlah_buku += 1
    def __str__(self):
        return f"{self.judulbuku}, {self.penulisbuku}, {self.tahun}"
    def ubah(self, ubah):
        self.tahun += ubah
B1 = Buku("A Bridge Too Far", "Nino Oktorino", 2017)
print(B1)
B1.ubah(1)
print(B1)
B2 = Buku("Lost In The Jungle", "Yossi Ghinsberg", 2018)
print(B2)
B2.ubah(2)
print(B2)