<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Account</title>
    <link
      href="https://unpkg.com/boxicons@2.1.1/css/boxicons.min.css"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="css/app.css" />
    <link rel="stylesheet" href="/css/style.css"/>

  </head>

  <body>
  <div class="main">
        <div class="navbar">
            <div class="menu">
                <ul>
                    <li><a href="/watch.php">WATCH</a></li>
                    <li><a href="/play.php">PLAY NOW!</a></li>
                    <li><a href="/homepage.php">Home Page</a></li>

                </ul>
            </div>
        </div>
        <form action="update_profile" method="post">
                <h2 class="title">Your Shift Profile</h2>
                <div class="input-field">
                    <i class="bx bxs-user"></i>
                    <input type="text" placeholder="Username" name="username" />
                </div>
                <div class="input-field">
                    <i class="bx bxs-envelope"></i>
                    <input type="text" placeholder="Email" name="email" />
                </div>
                <div class="input-field">
                    <i class="bx bxs-lock-alt"></i>
                    <input type="password" placeholder="Current Password" name="current_password" />
                </div>
                <div class="input-field">
                    <i class="bx bxs-lock-alt"></i>
                    <input type="password" placeholder="New Password" name="new_password" />
                </div>
                    <input type="submit" value="Update Profile" class="btn solid" />
        
    </form>
  </div>
  </body>
</html>
