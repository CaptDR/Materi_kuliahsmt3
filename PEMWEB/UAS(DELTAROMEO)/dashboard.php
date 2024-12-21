<?php
session_start();

// Cek apakah pengguna sudah login, jika tidak, redirect ke login.html
if (!isset($_SESSION['username']) || !isset($_SESSION['role'])) {
    header("Location: login.html");
    exit();
}

$username = $_SESSION['username'];
$role = $_SESSION['role'];
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DASHBOARD DELTAROMEO</title>
    <link rel="shortcut icon" href="img/favicon.png" type="image/x-icon">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <script>
        function redirectPage() {
            const selectedOption = document.getElementById('type').value;
            if (selectedOption === 'sewa') {
                window.location.href = 'sewa.html';
            } else if (selectedOption === 'tour') {
                window.location.href = 'tour.html';
            } else if (selectedOption === 'complain') {
                window.location.href = 'complain.html';
            } else if (selectedOption === '') {
                alert('Pilih salah satu layanan');
            }
        }
    </script>
</head>

<body>
    <nav class="navbar bg-light justify-content-center">
        <a class="navbar-brand" href="index.html">
            <img src="img/logo.png" alt="DELTAROMEO OUTDOOR" width="42" height="42" class="d-inline-block mt--2 me-2">
            <span class="text-body fs-4 fw-bolder">DELTAROMEO</span>
        </a>
    </nav>

    <nav class="navbar bg-light justify-content-end">
        <span class="me-3 text-dark fw-bold">
            Welcome, <?php echo ($username); ?>
        </span>
        <a href="login.html" class="btn btn-danger btn-sm">Logout</a>
    </nav>

    <form onsubmit="redirectPage(); return false;">
        <div class="mb-3">
            <select class="form-select" id="type" required>
                <option value="" disabled selected>--Pilih layanan--</option>
                <option value="sewa">Sewa Alat Camping</option>
                <option value="tour">Jasa Tour Guide</option>
                <option value="complain">Complain</option>
            </select>
        </div>
        <div class="d-flex justify-content-center">
            <button type="submit" class="btn btn-primary">Lanjut</button>
        </div>
    </form>
</body>

</html>
