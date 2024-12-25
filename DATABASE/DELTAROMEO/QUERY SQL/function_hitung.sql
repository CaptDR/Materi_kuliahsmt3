DELIMITER //
CREATE FUNCTION calculate_user_spending (p_user_id INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE total_spending DECIMAL(10,2);

    -- Hitung total pengeluaran
    SELECT SUM(total_harga) INTO total_spending
    FROM transactions
    WHERE user_id = p_user_id;

    RETURN IFNULL(total_spending, 0);
END //
DELIMITER ;
