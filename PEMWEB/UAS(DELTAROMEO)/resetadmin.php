<?php
// Menghubungkan ke database
$server = "localhost";
$user = "root";
$pass = "";
$db = "userdelta";

$conn = new mysqli($server, $user, $pass, $db);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Password baru untuk admin
$new_password = 'admin123'; // Password asli
$hashed_password = password_hash($new_password, PASSWORD_DEFAULT);

// Update password untuk user dengan username 'admin'
$query = "UPDATE users SET password = '$hashed_password' WHERE username = 'admin'";
if ($conn->query($query) === TRUE) {
    echo "Password admin berhasil diperbarui!";
} else {
    echo "Error: " . $conn->error;
}

// Menutup koneksi ke database
$conn->close();
?>