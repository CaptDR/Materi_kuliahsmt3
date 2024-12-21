<?php
require 'db_connect.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nama_barang = $_POST['nama_barang'];
    $harga = $_POST['harga'];
    $stok = $_POST['stok'];

    $query = "INSERT INTO barang (nama_barang, harga, stok) VALUES ('$nama_barang', '$harga', '$stok')";
    if ($conn->query($query)) {
        header('Location: dashboardadmin.php');
        exit;
    } else {
        echo "Error: " . $conn->error;
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tambah Barang Sewaan</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Tambah Barang Sewaan</h1>
    <form method="POST" action="">
        <label>Nama Barang:</label><br>
        <input type="text" name="nama_barang" required><br>
        <label>Harga:</label><br>
        <input type="number" name="harga" required><br>
        <label>Stok:</label><br>
        <input type="number" name="stok" required><br>
        <button type="submit">Simpan</button>
    </form>
</body>
</html>
