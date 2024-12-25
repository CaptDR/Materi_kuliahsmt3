CREATE TABLE transactions3nf(
transaction_id VARCHAR(50) PRIMARY KEY,
user_id VARCHAR(50) NOT NULL,
total_harga DECIMAL(10,2) NOT NULL,
status_id INT NOT NULL,
created_at DATETIME NOT NULL,
FOREIGN KEY(status_id) REFERENCES transaction_status(status_id))