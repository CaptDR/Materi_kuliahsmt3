class User:
    def __init__(self, username, email, user_id):
        self.username = username
        self.email = email
        self.user_id = user_id

    def login(self):
        print(f"User {self.username} with email {self.email} has logged in.")
    
    def logout(self):
        print(f"User {self.username} has logged out.")

# Turunan dari User
class BasicUser(User):
    def view_product(self, product_id):
        print(f"Displaying information for product with ID {product_id}.")
    
    def add_to_cart(self, product_id, qty):
        print(f"Added {qty} of product with ID {product_id} to cart.")

# Turunan dari BasicUser
class PremiumUser(BasicUser):
    def apply_voucher(self, voucher_code, cart_total):
        discount = cart_total * 0.10  # Contoh diskon 10%
        print(f"Voucher {voucher_code} applied. Discounted total: {cart_total - discount}")
    
    def request_priority_support(self, issue_description):
        print(f"Priority support requested with issue: {issue_description}")

# Turunan dari User
class Seller(User):
    def add_product(self, product_name, description, price, stock):
        print(f"Product {product_name} added with description '{description}', price {price}, and stock {stock}.")
    
    def process_order(self, order_id, status):
        print(f"Order {order_id} has been updated to status: {status}.")

# Turunan dari User
class Admin(User):
    def remove_user(self, user_id):
        print(f"User with ID {user_id} has been removed from the system.")
    
    def generate_report(self, report_type, start_date, end_date):
        print(f"Generating {report_type} report from {start_date} to {end_date}.")


# Pembuatan objek Seller
seller = Seller("sellerPro", "seller@example.com", 202)
seller.login()
product_name = input("Enter product name: ")
description = input("Enter product description: ")
price = float(input("Enter product price: "))
stock = int(input("Enter product stock: "))
seller.add_product(product_name, description, price, stock)
order_id = input("Enter order ID to process: ")
status = input("Enter order status (e.g., 'in shipment' or 'completed'): ")
seller.process_order(order_id, status)
seller.logout()

# Pembuatan objek PremiumUser
premium_user = PremiumUser("Buddy-Anduk", "buddy22@example.com", 101)
premium_user.login()
product_id = input("Enter product ID to view: ")
premium_user.view_product(product_id)
product_id = input("Enter product ID to add to cart: ")
qty = int(input("Enter quantity to add to cart: "))
premium_user.add_to_cart(product_id, qty)
voucher_code = input("Enter voucher code: ")
cart_total = float(input("Enter cart total: "))
premium_user.apply_voucher(voucher_code, cart_total)
issue_description = input("Describe the issue for priority support: ")
premium_user.request_priority_support(issue_description)
premium_user.logout()