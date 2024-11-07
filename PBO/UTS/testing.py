# Kelas Dasar User
class User:
    def __init__(self, username, email, user_id):
        self.username = username
        self.email = email
        self.user_id = user_id

    def login(self):
        print(f"{self.username} berhasil login dengan email {self.email}")

    def logout(self):
        print(f"{self.username} berhasil logout")

# Turunan Pertama BasicUser dari User
class BasicUser(User):
    def view_product(self, product_id):
        print(f"Menampilkan informasi produk dengan ID {product_id}")

    def add_to_cart(self, product_id, qty):
        print(f"Menambahkan produk dengan ID {product_id} ke keranjang belanja sebanyak {qty} item")

# Turunan Kedua PremiumUser dari BasicUser (Multilevel Inheritance)
class PremiumUser(BasicUser):
    def apply_voucher(self, voucher_code, cart_total):
        print(f"Menerapkan voucher {voucher_code} pada total belanja {cart_total}")

    def request_priority_support(self, issue_description):
        print(f"Menghubungi dukungan prioritas untuk masalah: {issue_description}")

# Turunan Kelas User lainnya, Seller (Hierarchy Inheritance)
class Seller(User):
    def add_product(self, product_name, description, price, stock):
        print(f"Menambahkan produk: {product_name} dengan deskripsi '{description}', harga {price}, stok {stock}")

    def process_order(self, order_id, status):
        print(f"Memproses pesanan ID {order_id} dengan status '{status}'")

# Turunan Kelas User lainnya, Admin (Hierarchy Inheritance)
class Admin(User):
    def remove_user(self, user_id):
        print(f"Menghapus pengguna dengan ID {user_id} dari sistem")

    def generate_report(self, report_type, start_date, end_date):
        print(f"Menghasilkan laporan '{report_type}' dari {start_date} hingga {end_date}")

# Membuat objek PremiumUser
premium_user = PremiumUser("Buddy-Anduk", "buddy22@example.com", 101)

# Menggunakan metode pada objek PremiumUser
premium_user.login()
premium_user.view_product(1001)
premium_user.add_to_cart(1001, 2)
premium_user.apply_voucher("DISC10", 500000)
premium_user.request_priority_support("Produk yang dipesan rusak")
premium_user.logout()

print("\n" + "="*40 + "\n")

# Membuat objek Seller
seller = Seller("sellerPro", "seller@example.com", 202)

# Menggunakan metode pada objek Seller
seller.login()
seller.add_product("Sepatu Hiking", "Sepatu tahan air untuk hiking", 750000, 50)
seller.process_order(1234, "dalam pengiriman")
seller.logout()