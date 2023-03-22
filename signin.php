<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SignIn__SignUp</title>
    <link href="https://unpkg.com/boxicons@2.1.1/css/boxicons.min.css" rel="stylesheet" />
    <link rel="stylesheet" href="css/app.css" />
</head>

<body>
    <div class="container">
        <div class="forms-container">
            <div class="signin-signup">
                <form class="sign-in-form" action="login.php" method="post">
                    <h2 class="title">Log In</h2>
                    <div class="input-field">
                        <i class="bx bxs-user"></i>
                        <input type="text" placeholder="Username" name="name" />
                    </div>
                    <div class="input-field">
                        <i class="bx bxs-lock-alt"></i>
                        <input type="password" placeholder="Password" name="password" />
                    </div>
                    <input type="submit" value="Login" class="btn solid" />
                    <p class="social-text">Or sign in with social platforms</p>

                    <div class="social-media">
                        <a href="#" class="social-icon">
                            <i class="bx bxl-facebook"></i>
                        </a>
                        <a href="#" class="social-icon">
                            <i class="bx bxl-twitter"></i>
                        </a>
                        <a href="#" class="social-icon">
                            <i class="bx bxl-google"></i>
                        </a>
                        <a href="#" class="social-icon">
                            <i class="bx bxl-linkedin"></i>
                        </a>
                    </div>
                </form>
                <form class="sign-up-form" action="homePage.php" method="post">
                    <h2 class="title">Sign Up</h2>
                    <div class="input-field">
                        <i class="bx bxs-user"></i>
                        <input type="text" placeholder="Username" name="name" />
                    </div>
                    <div class="input-field">
                        <i class="bx bxs-envelope"></i>
                        <input type="text" placeholder="Email" name="email" />
                    </div>
                    <div class="input-field">
                        <i class="bx bxs-lock-alt"></i>
                        <input type="password" placeholder="Password" name="password" />
                    </div>
                    <input type="submit" value="Sign Up" class="btn solid" />
                    <p class="social-text">Or sign up with social platforms</p>

                    <div class="social-media">
                        <a href="#" class="social-icon">
                            <i class="bx bxl-facebook"></i>
                        </a>
                        <a href="#" class="social-icon">
                            <i class="bx bxl-twitter"></i>
                        </a>
                        <a href="#" class="social-icon">
                            <i class="bx bxl-google"></i>
                        </a>
                        <a href="#" class="social-icon">
                            <i class="bx bxl-linkedin"></i>
                        </a>
                    </div>
                </form>
            </div>
        </div>
        <div class="panels-container">
            <div class="panel left-panel">
                <div class="content">
                    <h3>Don't have an account?</h3>
                    <p></p>
                    <button class="btn transparent" id="sign-up-btn">Sign up</button>
                </div>
                <img src="/images/Profiling_Monochromatic1.png" class="image" alt="" />
            </div>
            <div class="panel right-panel">
                <div class="content">
                    <h3>Already have an account?</h3>
                    <p></p>
                    <button class="btn transparent" id="sign-in-btn">Login in</button>
                </div>
                <img src="/images/Profiling_Monochromatic1.png" class="image" alt="" />
            </div>
        </div>
    </div>
    <script src="js/app.js"></script>



    <?php
    //signing up php.
    $name = $_POST['name'];
    $email = $_POST['email'];
    $password = $_POST['password'];



    //DATABASE connection

    $conn = new mysqli('eu-cdbr-west-03.cleardb.net', 'b1f91cc87f0529', 'fee6eb8a', 'heroku_63291ad8f31606c');
    if ($conn->connect_error) {
        die('Connection Failed : ' . $conn->connect_error);
    } else {
        $stmt = $conn->prepare("insert into users(name,email,password) values (?,?,?)");
        $stmt->bind_param("sss", $name, $email, $password);
        $stmt->execute();
        header("Location: homePage.php");
        $stmt->close();
        $conn->close();
    }
    ?>


    <?php
    //php for loging in

    $name = $_POST['name'];
    $password = $_POST['password'];


    //DATABASE connection

    $conn = new mysqli('eu-cdbr-west-03.cleardb.net', 'b1f91cc87f0529', 'fee6eb8a', 'heroku_63291ad8f31606c');
    if ($conn->connect_error) {
        die('Connection Failed : ' . $conn->connect_error);
    } else {
        $stmt = $conn->prepare("select * FROM users where name = ? and password = ?");
        $stmt->bind_param("ss", $name, $password);
        $stmt->execute();



        $stmt->close();
        $conn->close();
    }

    ?>




</body>

</html>