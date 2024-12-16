<!-- KONEKSI DATABASE -->
<?php 
$host = "localhost";
$user = "root";
$pass = "";
$database = "sikampus";
$connect = mysqli_connect($host, $user, $pass, $database);
if (!$connect){
    die("Koneksi Gagal !".mysqli_connect_error());
}else{
    echo"Koneksi Berhasil";
}