<!DOCTYPE html>
<html>

<head>
	<link rel="stylesheet" type="text/css" href="static/login_style.css">
	<title>Login | Delta</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>


<body>

	<a href="http://www.delta.com/"><img id = "logo" src="images/delta.png"></a>

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

	<div id = "cloud_animation1">
		<marquee direction="left" scrolldelay="300"><img id = "cloud" src="images/cloud.png">
	</div>
	
</body>


</html>