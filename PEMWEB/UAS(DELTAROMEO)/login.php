<?php
session_start();

$server = "localhost";
$user = "root";
$pass = "";
$db = "deltaromeo";

// Koneksi Database
$conn = new mysqli($server, $user, $pass, $db);

// Cek apakah koneksi berhasil
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password']; // Ambil password dari form

    // Query untuk login dengan prepared statement untuk menghindari SQL injection
    $stmt = $conn->prepare("SELECT * FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows == 1) {
        $row = $result->fetch_assoc();
        
        // Memverifikasi password menggunakan password_verify
        if (password_verify($password, $row['password'])) {
            // Menyimpan data user ke session
            $_SESSION['username'] = $row['username'];
            $_SESSION['role'] = $row['role'];

            // Redirect berdasarkan role
            if ($row['role'] == 'admin') {
                header("Location: dashboardadmin.php"); // Redirect ke dashboard admin
                exit();
            } else {
                ($row['role'] == 'user');
                header("Location: dashboard.php"); // Redirect ke dashboard user biasa
                exit();
            }
        } else {
            echo "Username atau Password salah!";
        }
    } else {
        echo "Username atau Password salah!";
    }

    $stmt->close();
}

$conn->close();
?>
