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

    def viewProduct(self):
        print(f"Show Product From ProductID {self.IDP}, the name of product is {self.namep}")
    
    def addToCart(self):
        print(f"Product {self.namep} with ProductID {self.IDP} and quantity {self.qty} added to cart")


class PremiumUser(BasicUser):
    def __init__(self, username, email, userId, IDP, qty, namep, vcc, cartqty):
        super().__init__(username, email, userId, IDP, qty, namep)
        self.voc = vcc  # Voucher Code
        self.cart = cartqty  # Cart Quantity

    def applyVoucher(self, voucherCode, cartTotal):
        # Check if the provided voucher code matches user's voucher code
        if voucherCode == self.voc:
            discount = 0.1  # Apply a 10% discount
            discountedTotal = cartTotal * (1 - discount)
            print(f"Voucher applied! New total after discount: {discountedTotal}")
        else:
            print("Invalid voucher code. Unable to apply discount.")

    def requestPrioritySupport(self, issueDescription):
        print(f"Priority support requested for issue: {issueDescription}")


class Seller(User):
    def __init__(self, username, email, userId):
        super().__init__(username, email, userId)
        self.products = {}  # Dictionary to store product information

    def addProduct(self, productName, description, price, stock):
        # Add a new product to the products dictionary
        productID = len(self.products) + 1  # Generate a new product ID
        self.products[productID] = {
            "productName": productName,
            "description": description,
            "price": price,
            "stock": stock
        }
        print(f"Product '{productName}' added with ID {productID}.")

    def processOrder(self, orderId, status):
        # Process an order by changing its status
        print(f"Order ID {orderId} status has been updated to '{status}'.")


# Creating an object for PremiumUser
premium_user = PremiumUser("buddy-Anduk", "buddy22@example.com", 101, IDP="P001", qty=2, namep="Smartphone", vcc="DISC20", cartqty=2)
premium_user.viewProduct()
premium_user.addToCart()
premium_user.applyVoucher(voucherCode="DISC20", cartTotal=500000)
premium_user.requestPrioritySupport("Need help with product issue")

# Creating an object for Seller
seller = Seller("sellerPro", "seller@example.com", 202)
seller.addProduct("Laptop", "High-performance laptop for professionals", 15000000, 5)
seller.processOrder("O124", "In Shipment")
