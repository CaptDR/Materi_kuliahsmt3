#Function diskon 10% untuk pembelian > 100.000#
DELIMITER $$
CREATE FUNCTION hitung_diskon(total_pembelian INT)
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE diskon INT;
	IF total_pembelian > 100000 THEN
		SET diskon = total_pembelian * 0.1;
	ELSE
		SET diskon = 0;
	END IF;
	RETURN diskon;
END$$
DELIMITER;