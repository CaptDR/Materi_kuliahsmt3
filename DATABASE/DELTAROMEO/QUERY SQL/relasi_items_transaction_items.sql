ALTER TABLE tbl_transactions_detail
ADD CONSTRAINT fk_items_transaction_items
FOREIGN KEY (item_id) REFERENCES barang(id_barang)
ON DELETE CASCADE ON UPDATE CASCADE