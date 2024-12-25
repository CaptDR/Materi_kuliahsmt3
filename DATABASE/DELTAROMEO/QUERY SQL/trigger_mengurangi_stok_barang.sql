DELIMITER //
CREATE TRIGGER after_insert_transaction_item
AFTER INSERT ON transactions_items
FOR EACH ROW
BEGIN
    -- Kurangi stok barang
    UPDATE items
    SET stok = stok - NEW.quantity
    WHERE item_id = NEW.id_barang;
END //
DELIMITER ;
