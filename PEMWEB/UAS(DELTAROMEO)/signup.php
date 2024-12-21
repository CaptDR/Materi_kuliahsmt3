<?php
$host = "localhost";
$user = "root";
$password = "";
$database = "deltaromeo";

$conn = new mysqli($host, $user, $password, $database);

// Mengecek koneksi ke database
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Validasi input (pastikan tidak kosong)
    if (!empty($username) && !empty($password)) {
        // Hash password sebelum disimpan
        $hashed_password = password_hash($password, PASSWORD_DEFAULT);

        // Menggunakan prepared statements untuk menghindari SQL Injection
        $stmt = $conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
        $stmt->bind_param("ss", $username, $hashed_password);

        // Menjalankan query
        if ($stmt->execute()) {
            // Mengarahkan pengguna ke halaman login setelah registrasi berhasil
            echo "<script>
            alert('Registrasi berhasil!');
            window.location.href = 'login.html';</script>";
            exit();
        } else {
            echo "Error: " . $stmt->error;
        }

        // Menutup prepared statement
        $stmt->close();
    } else {
        echo "Username dan password harus diisi!";
    }
}

// Menutup koneksi ke database
$conn->close();
?>