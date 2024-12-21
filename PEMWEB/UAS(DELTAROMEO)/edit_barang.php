<?php
require 'db_connect.php';

$id = $_GET['id'];
$query = "SELECT * FROM barang WHERE id = $id";
$result = $conn->query($query);
$barang = $result->fetch_assoc();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nama_barang = $_POST['nama_barang'];
    $harga = $_POST['harga'];
    $stok = $_POST['stok'];

    $query = "UPDATE barang SET nama_barang='$nama_barang', harga='$harga', stok='$stok' WHERE id=$id";
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
    <title>Edit Barang Sewaan</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Edit Barang Sewaan</h1>
    <form method="POST" action="">
        <label>Nama Barang:</label><br>
        <input type="text" name="nama_barang" value="<?= $barang['nama_barang'] ?>" required><br>
        <label>Harga:</label><br>
        <input type="number" name="harga" value="<?= $barang['harga'] ?>" required><br>
        <label>Stok:</label><br>
        <input type="number" name="stok" value="<?= $barang['stok'] ?>" required><br>
        <button type="submit">Update</button>
    </form>
</body>
</html>
