<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="login_style.css">
	<title>Login | Delta</title>
</head>


<body>
	<img id = "logo" src="images/delta.png">
	
	<div id = "login_form">
		<form action="login.php"  method = "GET">

			<h2 align="center"><span id = "login_text">Login to My Delta</span></h2>

			<span id= "all_fields">All fields are required. </span><br><br>

			<span id = "custom_word">Username:</span><br>
			<input type = "text" name = "username" placeholder="Enter SkyMiles number or username"><br>
			
			<span id = "custom_word">Password:</span><br>
			<input type = "password" name = "password" placeholder="Enter password">
			<br><br>
			
			<input type = "submit" name = "submit" value = "Log in">
		</form>
	</div>
	
</body>


</html>