ALTER TABLE transactions
ADD CONSTRAINT fk_status_transactions
FOREIGN KEY (status_order) REFERENCES transaction_status(status_id)
ON DELETE CASCADE ON UPDATE CASCADE;
