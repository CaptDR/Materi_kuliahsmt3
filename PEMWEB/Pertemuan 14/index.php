<?php
// Memanggil File dbConnection.php sebagai Global Var
include "dbConnection.php";

// Membuat Operasi Delete Data
if (isset($_GET['delete'])) {
    $nim = $_GET['delete'];
    $sql = "DELETE FROM tbl_mahasiswa WHERE nim = '$nim'";
    $connect->query($sql);
    header("Location: index.php");
    exit();
}

// Membuat Operasi Edit (Mengambil Data untuk Form)
$editData = null;
if (isset($_GET['edit'])) {
    $nim = $_GET['edit'];
    $result = $connect->query("SELECT * FROM tbl_mahasiswa WHERE nim = '$nim'");
    if ($result->num_rows > 0) {
        $editData = $result->fetch_assoc();
    }
}

// Membuat Operasi Insert dan Update
if (isset($_POST['submit'])) {
    $nim = $_POST['nim'];
    $nama = $_POST['nama'];
    $jurusan = $_POST['jurusan'];

    // Periksa apakah ini mode EDIT atau INSERT
    if (isset($_POST['edit_nim']) && $_POST['edit_nim'] != '') {
        // Mode Edit: Update Data
        $edit_nim = $_POST['edit_nim'];
        $sql = "UPDATE tbl_mahasiswa SET nim = '$nim', nama = '$nama', jurusan = '$jurusan' WHERE nim = '$edit_nim'";
    } else {
        // Mode Insert: Tambahkan Data Baru
        $sql = "INSERT INTO tbl_mahasiswa (nim, nama, jurusan) VALUES ('$nim', '$nama', '$jurusan')";
    }

    // Eksekusi Query
    if ($connect->query($sql) === TRUE) {
        header("Location: index.php");
        exit();
    } else {
        echo "Error: " . $connect->error;
    }
}

// Membuat Form Mahasiswa
function formMahasiswa($data = null)
{
    $editNim = $data ? $data['nim'] : ''; // Menyimpan nim lama untuk edit
    $id = $data ? $data['nim'] : '';
    $name = $data ? $data['nama'] : '';
    $jurusan = $data ? $data['jurusan'] : '';
    $buttonLabel = $data ? 'Update' : 'Submit';
    echo "
    <h1>Form Mahasiswa</h1>
    <form method='POST'>
        <table border='1'>
            <tr>
                <td><label for='nim'>NIM</label></td>
                <td><input type='text' value='$id' name='nim' id='nim' required></td>
            </tr>
            <tr>
                <td><label for='nama'>NAMA</label></td>
                <td><input type='text' name='nama' value='$name' id='nama' required></td>
            </tr>
            <tr>
                <td><label for='jurusan'>JURUSAN</label></td>
                <td><input type='text' name='jurusan' value='$jurusan' id='jurusan' required></td>
            </tr>
            <tr>
                <td></td>
                <td>
                    <button type='submit' name='submit'>$buttonLabel</button>
                    <input type='hidden' name='edit_nim' value='$editNim'>
                </td>
            </tr>
        </table>
    </form>";
}

// Fungsi Tampil Tabel Mahasiswa
function tampilTabel($connect)
{
    echo "
    <h1>Tabel Mahasiswa</h1>
    <table border='1'>
        <tr>
            <th>No</th>
            <th>NIM</th>
            <th>NAMA</th>
            <th>JURUSAN</th>
            <th>Aksi</th>
        </tr>
    ";
    $result = $connect->query("SELECT * FROM tbl_mahasiswa");
    if ($result->num_rows > 0) {
        $no = 1;
        while ($row = $result->fetch_assoc()) {
            echo "
            <tr>
                <td>{$no}</td>
                <td>{$row['nim']}</td>
                <td>{$row['nama']}</td>
                <td>{$row['jurusan']}</td>
                <td>
                    <a href='?delete={$row['nim']}' onClick='return confirm(\"Are you sure?\")'>Delete</a>
                    <a href='?edit={$row['nim']}'>Edit</a>
                </td>
            </tr>
            ";
            $no++;
        }
    } else {
        echo "<tr><td colspan='5'>Tidak ada data</td></tr>";
    }
    echo "</table>";
}

// Panggil Fungsi
formMahasiswa($editData);
tampilTabel($connect);
?>
