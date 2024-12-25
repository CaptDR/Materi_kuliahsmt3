-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for deltaromeo1
CREATE DATABASE IF NOT EXISTS `deltaromeo1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `deltaromeo1`;

-- Dumping structure for table deltaromeo1.barang
CREATE TABLE IF NOT EXISTS `barang` (
  `id_barang` varchar(50) NOT NULL,
  `type_id` varchar(10) NOT NULL,
  `nama_barang` varchar(100) NOT NULL,
  `harga` varchar(10) NOT NULL,
  `stok` int NOT NULL,
  PRIMARY KEY (`id_barang`),
  KEY `type_id` (`type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table deltaromeo1.barang: ~3 rows (approximately)
REPLACE INTO `barang` (`id_barang`, `type_id`, `nama_barang`, `harga`, `stok`) VALUES
	('BRG001', '', 'Tenda', 'Rp50.000', 12),
	('BRG002', '', 'Kompor', 'Rp20.000', 10),
	('BRG003', '', 'Sleeping Bag', 'Rp25.000', 10);

-- Dumping structure for table deltaromeo1.tbl_transactions_detail
CREATE TABLE IF NOT EXISTS `tbl_transactions_detail` (
  `transaction_detail_id` varchar(10) NOT NULL,
  `transaction_id` varchar(50) NOT NULL,
  `item_type` enum('tool','guide') NOT NULL,
  `item_id` varchar(10) NOT NULL,
  `quantitiy` int DEFAULT '1',
  `harga` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  PRIMARY KEY (`transaction_detail_id`),
  KEY `fk_transaction_items` (`transaction_id`),
  KEY `fk_items_transaction_items` (`item_id`),
  CONSTRAINT `fk_items_transaction_items` FOREIGN KEY (`item_id`) REFERENCES `barang` (`id_barang`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_transaction_items` FOREIGN KEY (`transaction_id`) REFERENCES `transactions` (`transaction_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tbl_transactions_detail_ibfk_1` FOREIGN KEY (`transaction_id`) REFERENCES `transactions` (`transaction_id`),
  CONSTRAINT `tbl_transactions_detail_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `barang` (`id_barang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table deltaromeo1.tbl_transactions_detail: ~0 rows (approximately)

-- Dumping structure for table deltaromeo1.tbl_type_barang
CREATE TABLE IF NOT EXISTS `tbl_type_barang` (
  `type_id` varchar(10) NOT NULL,
  `type_name` varchar(50) NOT NULL,
  PRIMARY KEY (`type_id`),
  CONSTRAINT `fk_item_type_items` FOREIGN KEY (`type_id`) REFERENCES `barang` (`type_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table deltaromeo1.tbl_type_barang: ~0 rows (approximately)

-- Dumping structure for table deltaromeo1.tour
CREATE TABLE IF NOT EXISTS `tour` (
  `id_guide` varchar(10) NOT NULL,
  `nama_guide` varchar(50) NOT NULL,
  `tujuan` varchar(50) NOT NULL,
  `durasi` varchar(20) NOT NULL,
  `harga` varchar(10) NOT NULL,
  PRIMARY KEY (`id_guide`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table deltaromeo1.tour: ~0 rows (approximately)

-- Dumping structure for table deltaromeo1.transactions
CREATE TABLE IF NOT EXISTS `transactions` (
  `transaction_id` varchar(50) NOT NULL,
  `user_id` int NOT NULL,
  `total_harga` decimal(10,2) NOT NULL,
  `status_order` varchar(50) NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `fk_user_transactions` (`user_id`),
  KEY `fk_status_transactions` (`status_order`),
  CONSTRAINT `fk_status_transactions` FOREIGN KEY (`status_order`) REFERENCES `transaction_status` (`status_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_user_transactions` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table deltaromeo1.transactions: ~0 rows (approximately)

-- Dumping structure for table deltaromeo1.transactions_items
CREATE TABLE IF NOT EXISTS `transactions_items` (
  `transaction_item_id` int NOT NULL AUTO_INCREMENT,
  `transaction_id` varchar(50) NOT NULL,
  `item_type` varchar(50) NOT NULL,
  `id_barang` varchar(50) NOT NULL,
  `quantity` int NOT NULL,
  `subtotal` varchar(50) NOT NULL,
  PRIMARY KEY (`transaction_item_id`),
  KEY `transaction_id` (`transaction_id`),
  KEY `id_barang` (`id_barang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table deltaromeo1.transactions_items: ~0 rows (approximately)

-- Dumping structure for table deltaromeo1.transaction_status
CREATE TABLE IF NOT EXISTS `transaction_status` (
  `status_id` varchar(50) NOT NULL,
  `status_name` varchar(10) NOT NULL,
  PRIMARY KEY (`status_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table deltaromeo1.transaction_status: ~0 rows (approximately)

-- Dumping structure for table deltaromeo1.users
CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `role` varchar(10) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table deltaromeo1.users: ~0 rows (approximately)

-- Dumping structure for view deltaromeo1.view_user_transactions
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `view_user_transactions` (
	`nama_pengguna` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`id_transaksi` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`total_harga_transaksi` DECIMAL(10,2) NOT NULL,
	`waktu_transaksi` DATETIME NOT NULL
) ENGINE=MyISAM;

-- Dumping structure for procedure deltaromeo1.add_transaction
DELIMITER //
CREATE PROCEDURE `add_transaction`(
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
END//
DELIMITER ;

-- Dumping structure for function deltaromeo1.calculate_user_spending
DELIMITER //
CREATE FUNCTION `calculate_user_spending`(p_user_id INT) RETURNS decimal(10,2)
    DETERMINISTIC
BEGIN
    DECLARE total_spending DECIMAL(10,2);

    -- Hitung total pengeluaran
    SELECT SUM(total_harga) INTO total_spending
    FROM transactions
    WHERE user_id = p_user_id;

    RETURN IFNULL(total_spending, 0);
END//
DELIMITER ;

-- Dumping structure for event deltaromeo1.delete_old_pending_transactions
DELIMITER //
CREATE EVENT `delete_old_pending_transactions` ON SCHEDULE EVERY 1 DAY STARTS '2024-12-25 18:29:35' ON COMPLETION NOT PRESERVE ENABLE DO BEGIN
    DELETE FROM transactions
    WHERE status_order = 'Pending' AND created_at < (NOW() - INTERVAL 7 DAY);
END//
DELIMITER ;

-- Dumping structure for trigger deltaromeo1.after_insert_transaction_item
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_insert_transaction_item` AFTER INSERT ON `transactions_items` FOR EACH ROW BEGIN
    -- Kurangi stok barang
    UPDATE items
    SET stok = stok - NEW.quantity
    WHERE item_id = NEW.id_barang;
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

-- Dumping structure for view deltaromeo1.view_user_transactions
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `view_user_transactions`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `view_user_transactions` AS select `u`.`username` AS `nama_pengguna`,`t`.`transaction_id` AS `id_transaksi`,`t`.`total_harga` AS `total_harga_transaksi`,`t`.`created_at` AS `waktu_transaksi` from (`users` `u` join `transactions` `t` on((`u`.`user_id` = `t`.`user_id`)));

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
