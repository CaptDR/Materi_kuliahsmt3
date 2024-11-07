class User:
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId
    def login(self):
        print(f"{self.username} ({self.email}) berhasil login")

    def logout(self):
        print(f"{self.username} berhasil logout")
        
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

class Admin(User):
    def __init__(self, username, email, userId):
        super().__init__(username, email, userId)
        self.users = {}  # Dictionary to store users information (for example purposes)

    def removeUser(self, userId):
        # Remove a user from the users dictionary based on userId
        if userId in self.users:
            del self.users[userId]
            print(f"User with ID {userId} has been removed.")
        else:
            print(f"No user found with ID {userId}.")

    def generateReport(self, reportType, startDate, endDate):
        # Generate a report based on report type and date range
        print(f"Generating {reportType} report from {startDate} to {endDate}.")


# Example Usage
# Creating a Seller
seller = Seller("seller01", "seller@example.com", "s01")
seller.login()
seller.addProduct("Laptop", "High performance laptop", 15000000, 10)
seller.processOrder("O123", "In Shipment")
seller.logout()

# Creating an Admin
admin = Admin("admin01", "admin@example.com", "a01")
admin.login()
admin.removeUser("s01")
admin.generateReport("transaction", "2023-01-01", "2023-12-31")
admin.logout()