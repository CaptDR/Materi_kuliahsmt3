DELIMITER //
CREATE PROCEDURE add_transaction (
    IN p_user_id INT,
    IN p_total_harga DECIMAL(10,2),
    IN p_status_order VARCHAR(50),
    IN p_created_at DATETIME,
    IN p_item_id VARCHAR(50),
    IN p_quantity INT,
    IN p_subtotal DECIMAL(10,2)
)
BEGIN
    -- Tambahkan transaksi ke tabel transactions
    INSERT INTO transactions (user_id, total_harga, status_order, created_at)
    VALUES (p_user_id, p_total_harga, p_status_order, p_created_at);

    -- Ambil ID transaksi terakhir
    SET @transaction_id = LAST_INSERT_ID();

    -- Tambahkan item ke tabel transaction_items
    INSERT INTO transaction_items (transaction_id, item_id, quantity, subtotal)
    VALUES (@transaction_id, p_item_id, p_quantity, p_subtotal);
END //
DELIMITER ;
