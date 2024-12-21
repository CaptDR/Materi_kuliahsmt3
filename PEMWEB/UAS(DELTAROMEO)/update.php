<?php
// Koneksi ke database
$host = "localhost";
$user = "root";
$password = "";
$database = "deltaromeo";

$conn = new mysqli($host, $user, $password, $database);

// Periksa koneksi
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Jika form update disubmit
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Ambil data dari form
    $username = $_POST['username'];
    $old_password = $_POST['old_password'];
    $new_password = $_POST['new_password'];
    $new_email = $_POST['new_email'];

    // Query untuk mengambil data user berdasarkan username
    $sql = "SELECT * FROM users WHERE username = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();

    // Jika user ditemukan
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        
        // Verifikasi password lama
        if (password_verify($old_password, $row['password'])) {
            // Hash password baru
            $hashed_password = password_hash($new_password, PASSWORD_DEFAULT);

            // Query untuk update password dan email
            $update_sql = "UPDATE users SET password = ?, email = ? WHERE username = ?";
            $update_stmt = $conn->prepare($update_sql);
            $update_stmt->bind_param("sss", $hashed_password, $new_email, $username);

            if ($update_stmt->execute()) {
                echo "<script>
                        alert('User berhasil diupdate!');
                        window.location.href = 'login.html'; // Redirect setelah update
                      </script>";
            } else {
                echo "Error: " . $update_stmt->error;
            }
        } else {
            // Password lama tidak cocok
            echo "Password lama tidak cocok.";
        }

        $update_stmt->close();
    } else {
        echo "User tidak ditemukan.";
    }

    $stmt->close();
}

// Tutup koneksi
$conn->close();
?>
