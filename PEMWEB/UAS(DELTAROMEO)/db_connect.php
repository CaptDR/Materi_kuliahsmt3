<?php
// Konfigurasi database
$host = "localhost";
$username = "root";
$password = "";
$database = "deltaromeo";

// Membuat koneksi
$conn = new mysqli($host, $username, $password, $database);

// Periksa koneksi
if ($conn->connect_error) {
    die("Koneksi gagal: " . $conn->connect_error);
}
?>
