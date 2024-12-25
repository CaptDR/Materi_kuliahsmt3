ALTER TABLE tbl_transactions_detail
ADD CONSTRAINT fk_transaction_items
FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id)
ON DELETE CASCADE ON UPDATE cascade