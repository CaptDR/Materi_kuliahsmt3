CREATE TABLE transactions_items(
transaction_item_id INT AUTO_INCREMENT PRIMARY KEY,
transaction_id VARCHAR(50) NOT NULL,
item_type VARCHAR(50) NOT NULL,
id_barang VARCHAR(50) NOT NULL,
FOREIGN KEY(transaction_id) REFERENCES transactions2nf(transaction_id))