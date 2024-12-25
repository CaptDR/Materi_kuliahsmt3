CREATE TABLE transactions1nf(
transaction_id VARCHAR(50) PRIMARY KEY,
user_id INT NOT NULL,
id_barang VARCHAR(50),
id_guide VARCHAR(50),
total_harga DECIMAL(10,2),
status_order VARCHAR(50) NOT NULL,
created_at DATETIME NOT NULL)