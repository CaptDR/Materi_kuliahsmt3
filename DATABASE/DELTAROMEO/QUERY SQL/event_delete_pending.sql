DELIMITER //
CREATE EVENT delete_old_pending_transactions
ON SCHEDULE EVERY 1 DAY
DO
BEGIN
    DELETE FROM transactions
    WHERE status_order = 'Pending' AND created_at < (NOW() - INTERVAL 7 DAY);
END //
DELIMITER ;