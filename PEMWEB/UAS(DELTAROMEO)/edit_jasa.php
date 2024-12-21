<?php
require 'db_connect.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nama_guide = $_POST['nama_guide'];
    $harga = $_POST['harga'];
    $pengalaman = $_POST['pengalaman'];

    $query = "INSERT INTO jasa (nama_guide, harga, pengalaman) VALUES ('$nama_guide', '$harga', '$pengalaman')";
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
    <title>Tambah Jasa Tour Guide</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Tambah Jasa Tour Guide</h1>
    <form method="POST" action="">
        <label>Nama Guide:</label><br>
        <input type="text" name="nama_guide" required><br>
        <label>Harga:</label><br>
        <input type="number" name="harga" required><br>
        <label>Pengalaman (dalam tahun):</label><br>
        <input type="number" name="pengalaman" required><br>
        <button type="submit">Simpan</button>
    </form>
</body>
</html>
