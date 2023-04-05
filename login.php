<?php
include('connection.php');
session_start();

$username = $_POST['username'];
$password = $_POST['password'];


$sql = "select * from users where username = '$username' and password = '$password'";
$result = mysqli_query($conn, $sql);
$count = mysqli_num_rows($result);




if ($count == 1) {
    $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
    $_SESSION['user_id'] = $row['userid'];
    header("Location: homePage.php");
} else {
    $message[] = "Login failed. Invalid username or password!";
}
