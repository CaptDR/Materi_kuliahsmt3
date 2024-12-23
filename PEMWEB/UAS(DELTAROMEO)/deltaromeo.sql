-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 23, 2024 at 08:45 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `deltaromeo`
--

-- --------------------------------------------------------

--
-- Table structure for table `barang`
--

CREATE TABLE `barang` (
  `id_brg` varchar(10) NOT NULL,
  `nama_barang` varchar(100) NOT NULL,
  `harga` varchar(15) NOT NULL,
  `stok` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `barang`
--

INSERT INTO `barang` (`id_brg`, `nama_barang`, `harga`, `stok`) VALUES
('BRG001', 'Tenda(4)', 'Rp50.000', '10'),
('BRG002', 'Sleeping Bag', 'Rp25.000', '15'),
('BRG003', 'Kompor Portable', 'Rp10.000', '10'),
('BRG004', 'Matras Tenda', 'Rp10.000', '10'),
('BRG005', 'Lampu Tenda', 'Rp10.000', '10');

-- --------------------------------------------------------

--
-- Table structure for table `jasa`
--

CREATE TABLE `jasa` (
  `id_guide` varchar(10) NOT NULL,
  `nama_guide` varchar(100) NOT NULL,
  `tujuan` varchar(100) NOT NULL,
  `durasi` varchar(50) NOT NULL,
  `harga` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `jasa`
--

INSERT INTO `jasa` (`id_guide`, `nama_guide`, `tujuan`, `durasi`, `harga`) VALUES
('GD001', 'Topan Rimba', 'Gunung Ciremai', '2 Hari 1 Malam', 'Rp2.500.000'),
('GD002', 'Awan Rimba', 'Pantai Pangandaran', '1 Hari', 'Rp1.000.000'),
('GD003', 'Topan Rawa', 'Taman Nasional Ujung Kulon', '3 Hari 2 Malam', 'Rp2.500.000');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','user') DEFAULT 'user',
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`, `email`) VALUES
(1, 'admin', '$2y$10$SiZxZlKm7rwDY.zunATOSuvvMfdMBU3C9e1ezjyi0aJBinFeB/Uf2', 'admin', 'dimas556.dm@gmail.com'),
(19, 'captdr', '$2y$10$yM3ociwVq1oRzXw92KvZbuHO07u6OnXa48CE9LzUGXnjvRBdQXdci', 'user', 'sayroosatrio@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
