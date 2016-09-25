<!DOCTYPE html>

<html>

<head>
	<link rel="stylesheet" type="text/css" href="uber_style.css">
	<title>Set-Up Uber Ride | Delta</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
</head>


<body>
	<img id = "logo" src="images/delta.png">

    <style>
        div {
            width: 100px;
            height: 100px;
            background-color: red;
            position: relative;
            -webkit-animation-name: example; /* Chrome, Safari, Opera */
            -webkit-animation-duration: 4s; /* Chrome, Safari, Opera */
            animation-name: example;
            animation-duration: 4s;
        }

        /* Chrome, Safari, Opera */
        @-webkit-keyframes example {
            0%   {background-color:red; left:0px; top:0px;}
            25%  {background-color:yellow; left:200px; top:0px;}
            50%  {background-color:blue; left:200px; top:200px;}
            75%  {background-color:green; left:0px; top:200px;}
            100% {background-color:red; left:0px; top:0px;}
        }

        /* Standard syntax */
        @keyframes example {
            0%   {background-color:red; left:0px; top:0px;}
            25%  {background-color:yellow; left:200px; top:0px;}
            50%  {background-color:blue; left:200px; top:200px;}
            75%  {background-color:green; left:0px; top:200px;}
            100% {background-color:red; left:0px; top:0px;}
        }
    </style>

	<div id = "dropdown_menu">

	</div>
	

</body>


</html>