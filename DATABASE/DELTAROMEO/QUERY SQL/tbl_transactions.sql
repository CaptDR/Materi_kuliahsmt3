CREATE TABLE transactions(
transaction_id VARCHAR(50) PRIMARY KEY NOT NULL,
user_id INT NOT NULL,
total_harga DECIMAL(10, 2) NOT NULL,
status_order VARCHAR(50) NOT NULL,
created_at DATETIME NOT NULL,
FOREIGN KEY (user_id) REFERENCES users (user_id))