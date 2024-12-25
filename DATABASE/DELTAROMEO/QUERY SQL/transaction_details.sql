CREATE TABLE tbl_transactions_detail(
transaction_detail_id VARCHAR(10) PRIMARY KEY,
transaction_id VARCHAR(50) NOT NULL,
item_type ENUM('tool', 'guide') NOT NULL,
item_id VARCHAR(10) NOT NULL,
quantitiy INT DEFAULT 1,
harga DECIMAL(10, 2) NOT NULL,
subtotal DECIMAL(10, 2) NOT NULL,
FOREIGN KEY (transaction_id) REFERENCES transactions (transaction_id))