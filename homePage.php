<?php

include 'connection.php';
session_start();
$user_id = $_SESSION['user_id'];

if (!isset($user_id)) {
    header('location:login.php');
};
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <title>Home Page</title>
    <link rel="stylesheet" href="/css/style.css">
</head>

<body>

    <div class="main">
        <div class="navbar">
            <div class="icon">
                <h5 class="logo">shift</h5>
            </div>

            <div class="menu">
                <ul>
                    <li><a href="/watch.php">SPECTATE</a></li>
                    <li> <a href="">MY PAST GAMES</a></li>
                    <li><a href="/play.php">PLAY NOW!</a></li>
                    <li><a href="/Account.php">ACCOUNT</a></li>

                </ul>
            </div>

            <div class="search">
                <input class="srch" type="search" name="" placeholder="search">
                <a href="#"> <button class="btn">Search</button></a>
            </div>

        </div>
        <div class="content">
            <h1>WELCOME <br><span>TO</span> <br>SHIFT</h1>
            <p class="par">
                <br>
            </p>

            <button class="cn"><a href="#">REFRESH</a></button>


        </div>
    </div>
    </div>
    </div>
    <script src="https://unpkg.com/ionicons@5.4.0/dist/ionicons.js"></script>

    <?php




    ?>









</body>

</html>