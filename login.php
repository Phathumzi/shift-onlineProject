<?php
include('connection.php');

$username = $_POST['username'];
$password = $_POST['password'];


$sql = "select * from users where username = '$username' and password = '$password'";
$result = mysqli_query($conn, $sql);
$row = mysqli_fetch_array($result, MYSQLI_ASSOC);
$count = mysqli_num_rows($result);




if ($count == 1) {
    header("Location: homePage.php");
} else {
    echo ("Login failed. Invalid username or password!");
}
