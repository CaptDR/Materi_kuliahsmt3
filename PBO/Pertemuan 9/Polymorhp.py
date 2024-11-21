#Tanpa Polymorph
class jumlah:
    def tambah1(n1, n2):
        print(f"Hasilnya    : {n1+n2}")
objek = jumlah
objek.tambah1(1,2)

#Implementasi Polymorph
class penjumlahan:
    def tambah2 (n1, n2):
        print(f"Hasilnya    : {n1+n2}")
objek1 = penjumlahan
objek1.tambah2(2,3)

#Polymorph 2
class penjumlahan3:
    def tambah3 (*args):
        return sum (args)
objek3 = penjumlahan3
print(f"Hasilnya    : {objek3.tambah3(2,3,3,12)}")

#Menggunakan Default Parameter
class default:
    def tambah4 (self, a, b=0, c=0, d=0, e=0):
        print(f"Hasilnya    : {a+b+c+d}")
objek4 = default
objek4.tambah4(2,4,2)