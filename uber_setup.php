<!DOCTYPE html>

<html>

<head>
	<link rel="stylesheet" type="text/css" href="uber_style.css">
	<title>Set-Up Uber Ride | Delta</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<script src="jquery-1.12.4.min.js"></script><script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
	<script>
		$(document).ready(function(){
			$("#flip").click(function(){
				$("#panel").slideDown("medium");
			});
		});
	</script>
</head>

<body>
	<img id = "logo" src="images/delta.png">
	
	<div class = "uber-form">
	
		<img id = "uber" src = "images/uber-full.png"><br>
		
		<form action = "uber_setup.php" method = "POST">
			Enter Pickup Location:<br>
			<input type = "text" value = "AIRPORT ADDRESS" readonly><br>
			Enter Destination:<br>
			<input type = "text" name = "destination"><br>
			
			<input type = "button" id = "flip" value = "Submit">
			
			<div id = "panel">
				BLAH
			</div>
		
		</form>
		
	</div>
	

</body>


</html>