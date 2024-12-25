ALTER TABLE tbl_type_barang
ADD CONSTRAINT fk_item_type_items
FOREIGN KEY (type_id) REFERENCES barang (type_id)
ON DELETE CASCADE ON UPDATE CASCADE