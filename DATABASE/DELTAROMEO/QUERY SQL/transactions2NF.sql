CREATE TABLE transactions2nf (
transaction_id VARCHAR(50) PRIMARY KEY,
user_id VARCHAR(50) NOT NULL,
total_harga DECIMAL(10,2),
status_order VARCHAR(50) NOT NULL,
created_at DATETIME NOT NULL)