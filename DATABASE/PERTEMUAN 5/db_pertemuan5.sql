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


-- Dumping database structure for penjualan
CREATE DATABASE IF NOT EXISTS `penjualan` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `penjualan`;

-- Dumping structure for table penjualan.tbl_barang
CREATE TABLE IF NOT EXISTS `tbl_barang` (
  `kode_barang` varchar(20) NOT NULL,
  `nama_barang` varchar(50) DEFAULT NULL,
  `harga` int DEFAULT NULL,
  PRIMARY KEY (`kode_barang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table penjualan.tbl_barang: ~7 rows (approximately)
REPLACE INTO `tbl_barang` (`kode_barang`, `nama_barang`, `harga`) VALUES
	('BRG_001', 'Indomie Goreng', 2500),
	('BRG_002', 'Indomie Goreng Jumbo', 3000),
	('BRG_003', 'Mie Sedaap Goreng', 2500),
	('BRG_004', 'Mie Sedap Soto', 2300),
	('BRG_005', 'Intermie Goreng', 1500),
	('BRG_006', 'Intermie Soto', 1500),
	('BRG_007', 'Pop Mie Ayam', 4500);

-- Dumping structure for table penjualan.tbl_detailtransaksi
CREATE TABLE IF NOT EXISTS `tbl_detailtransaksi` (
  `kode_faktur` varchar(20) DEFAULT NULL,
  `kode_barang` varchar(20) DEFAULT NULL,
  `qty` int DEFAULT NULL,
  KEY `kode_faktur` (`kode_faktur`),
  KEY `kode_barang` (`kode_barang`),
  CONSTRAINT `tbl_detailtransaksi_ibfk_1` FOREIGN KEY (`kode_faktur`) REFERENCES `tbl_faktur` (`kode_faktur`),
  CONSTRAINT `tbl_detailtransaksi_ibfk_2` FOREIGN KEY (`kode_barang`) REFERENCES `tbl_barang` (`kode_barang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table penjualan.tbl_detailtransaksi: ~7 rows (approximately)
REPLACE INTO `tbl_detailtransaksi` (`kode_faktur`, `kode_barang`, `qty`) VALUES
	('KD_001', 'BRG_001', 5),
	('KD_001', 'BRG_002', 8),
	('KD_001', 'BRG_003', 9),
	('KD_001', 'BRG_004', 3),
	('KD_002', 'BRG_005', 6),
	('KD_002', 'BRG_006', 6),
	('KD_003', 'BRG_007', 3);

-- Dumping structure for table penjualan.tbl_faktur
CREATE TABLE IF NOT EXISTS `tbl_faktur` (
  `kode_faktur` varchar(20) NOT NULL,
  `tanggal` date DEFAULT NULL,
  PRIMARY KEY (`kode_faktur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table penjualan.tbl_faktur: ~3 rows (approximately)
REPLACE INTO `tbl_faktur` (`kode_faktur`, `tanggal`) VALUES
	('KD_001', '2020-07-13'),
	('KD_002', '2020-07-13'),
	('KD_003', '2020-07-13');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
