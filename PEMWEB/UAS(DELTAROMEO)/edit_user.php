<?php
require 'db_connect.php';

$id = $_GET['id'];
$query = "SELECT * FROM users WHERE id = $id";
$result = $conn->query($query);
$user = $result->fetch_assoc();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['name'];
    $email = $_POST['email'];
    $role = $_POST['role'];

    $query = "UPDATE users SET username='$username', email='$email', role='$role' WHERE id=$id";
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
    <title>Edit Pengguna</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Edit Pengguna</h1>
    <form method="POST" action="">
        <label>Nama:</label><br>
        <input type="text" name="name" value="<?= $user['username'] ?>" required><br>
        <label>Email:</label><br>
        <input type="email" name="email" value="<?= $user['email'] ?>" required><br>
        <label>Role:</label><br>
        <select name="role" required>
            <option value="user" <?= $user['role'] === 'user' ? 'selected' : '' ?>>User</option>
            <option value="admin" <?= $user['role'] === 'admin' ? 'selected' : '' ?>>Admin</option>
        </select><br>
        <button type="submit">Update</button>
    </form>
</body>
</html>
