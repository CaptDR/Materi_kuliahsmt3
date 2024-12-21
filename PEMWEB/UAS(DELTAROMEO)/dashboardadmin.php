<?php
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard - DELTAROMEO Outdoor</title>
    <link rel="shortcut icon" href="img/favicon.png" type="image/x-icon">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #4CAF50;
            color: white;
            padding: 1rem;
            text-align: center;
        }

        nav ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
            text-align: center;
        }

        nav ul li {
            display: inline;
            margin: 0 10px;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }

        main {
            max-width: 1200px;
            margin: 20px auto;
            background: white;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }

        h1,
        h2 {
            color: #333;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        table th,
        table td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        table th {
            background-color: #4CAF50;
            color: white;
        }

        a.button {
            display: inline-block;
            margin-top: 10px;
            padding: 10px 20px;
            color: white;
            background-color: #4CAF50;
            text-decoration: none;
            border-radius: 4px;
        }

        a.button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <nav class="navbar bg-light justify-content-center">
        <a class="navbar-brand" href="index.html">
            <img src="img/logo.png" alt="DELTAROMEO OUTDOOR" width="42" height="42" class="d-inline-block mt--2 me-2">
            <span class="text-body fs-4 fw-bolder">DELTAROMEO</span>
        </a>
    </nav>
    <header>
        <h1>Admin Dashboard - DELTAROMEO Outdoor</h1>
        <nav>
            <ul>
                <li><a href="login.html">Logout</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section>
            <h2>Kelola Pengguna</h2>
            <a href="add_user.php" class="button">Tambah User</a>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nama</th>
                        <th>Email</th>
                        <th>Role</th>
                        <th>Aksi</th>
                    </tr>
                </thead>
                <tbody>
<?php
// Contoh query untuk mengambil data user
                    require 'db_connect.php';
                    $query = "SELECT * FROM users";
                    $result = $conn->query($query);

                    while ($row = $result->fetch_assoc()) {
                        echo "<tr>";
                        echo "<td>" . $row['id'] . "</td>";
                        echo "<td>" . $row['username'] . "</td>";
                        echo "<td>" . $row['email'] . "</td>";
                        echo "<td>" . $row['role'] . "</td>";
                        echo "<td><a href='edit_user.php?id=" . $row['id'] . "'>Edit</a> | <a href='delete_user.php?id=" . $row['id'] . "'>Hapus</a></td>";
                        echo "</tr>";
                    }
                    ?>
                </tbody>
            </table>
        </section>

        <section>
            <h2>Kelola Barang Sewaan</h2>
            <a href="add_barang.php" class="button">Tambah Barang</a>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nama Barang</th>
                        <th>Harga</th>
                        <th>Stok</th>
                        <th>Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    <?php
                    // Contoh query untuk barang sewaan
                    $query = "SELECT * FROM barang";
                    $result = $conn->query($query);

                    while ($row = $result->fetch_assoc()) {
                        echo "<tr>";
                        echo "<td>" . $row['id_brg'] . "</td>";
                        echo "<td>" . $row['nama_barang'] . "</td>";
                        echo "<td>" . $row['harga'] . "</td>";
                        echo "<td>" . $row['stok'] . "</td>";
                        echo "<td><a href='edit_barang.php?id=" . $row['id_brg'] . "'>Edit</a> | <a href='delete_barang.php?id=" . $row['id_brg'] . "'>Hapus</a></td>";
                        echo "</tr>";
                    }
                    ?>
                </tbody>
            </table>
        </section>

        <section>
            <h2>Kelola Jasa Tour Guide</h2>
            <a href="add_jasa.php" class="button">Tambah Jasa</a>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nama Guide</th>
                        <th>Tujuan</th>
                        <th>Durasi</th>
                        <th>Harga</th>
                        <th>Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    <?php
                    // Contoh query untuk jasa tour guide
                    $query = "SELECT * FROM jasa";
                    $result = $conn->query($query);

                    while ($row = $result->fetch_assoc()) {
                        echo "<tr>";
                        echo "<td>" . $row['id_guide'] . "</td>";
                        echo "<td>" . $row['nama_guide'] . "</td>";
                        echo "<td>" . $row['tujuan'] . "</td>";
                        echo "<td>" . $row['durasi'] . "</td>";
                        echo "<td>" . $row['harga'] . "</td>";
                        echo "<td><a href='edit_jasa.php?id=" . $row['id_guide'] . "'>Edit</a> | <a href='delete_jasa.php?id=" . $row['id_guide'] . "'>Hapus</a></td>";
                        echo "</tr>";
                    }
                    ?>
                </tbody>
            </table>
        </section>
    </main>

</body>

</html>