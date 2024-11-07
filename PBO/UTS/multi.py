class User:
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId
        def login(self):
            print(f"{self.username} ({self.email}) berhasil login")

def logout(self):
    print(f"{self.username} berhasil logout")

class BasicUser(User):
    def __init__(self, username, email, userId, IDP, qty, namep):
        super().__init__(username, email, userId)
        self.IDP = IDP
        self.qty = qty
        self.namep = namep
    def viewpr(self):
        print(f"Show Product From ProductID {self.IDP} the name of product is {self.namep}")
    
    def addCart(self):
        print(f"Produk {self.namep} With ProductID {self.IDP} with total {self.qty} qty is added to cart")
namep = input("Masukkan Nama Produk : ")
qty = input("Masukkan Jumlah QTY Produk : ")
user = BasicUser(namep, qty)
user.addCart()

class PremiumUser(BasicUser):
    def __init__(self, username, email, userId, IDP, qty, namep, vcc, cartqty):
        super().__init__(username, email, userId, IDP, qty, namep)
        self.voc = vcc
        self.cart = cartqty
    
    def applyVoucher(self, vcc, cartqty):
        if vcc == self.voc:
            discount = 0.1
            discountTotal = cartqty * (1-discount)
            print(f"Voucher Applied! New Total After Discount {discountTotal}")
        else:
            print(f"Invalid Voucher")
    
    def request(self, issue)
        print(f"Priority Support Requested for issue : {issue}")

    
username = input("Masukkan Username :")
email = input("Masukkan Email: ")
userId = input("Masukkan User ID: ")
IDP = input("Masukkan Product ID: ")
qty = int(input("Masukkan Jumlah QTY Produk: "))
namep = input("Masukkan Nama Produk: ")
vcc = input("Masukkan Voucher Code: ")
cartqty = int(input("Masukkan Jumlah Cart Quantity: "))

premium_user = PremiumUser(username, email, userId, IDP, qty, namep, vcc, cartqty)
premium_user.addCart()
premium_user.applyVoucher(voucherCode="DISC10", cartTotal=100000)
premium_user.requestPrioritySupport("Need help with product delivery.")