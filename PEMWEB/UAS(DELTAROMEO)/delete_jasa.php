<?php
require 'db_connect.php';

$id = $_GET['id'];
$query = "DELETE FROM jasa WHERE id=$id";
if ($conn->query($query)) {
    header('Location: dashboardadmin.php');
    exit;
} else {
    echo "Error: " . $conn->error;
}
?>
