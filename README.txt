#About
This is a web app built at Hack GT 2016 by Jay Brooks, Forest Wong, Lawrence Chen, and Mitchell Lee. This app simulates a system where Delta Airline customers can spend their skymiles on lyft rides from the airport. It was entered in the Delta Corporate Customer Challenge where the goal was to improve the experience for corporate customers and other frequent flyers. It was built with SQL lite and flask

#How it works
Upon loggin in, our app look up the gets the from the Delta api. Some of the information had to be made up as the Delta api did not give us enough user information for our demo. The dashboard would show a list of flights for the user with the option to reserve a lyft ride for that flight. Once the user clicked the lyft option, the user would then be redirected to a form to fill out the ride information. The airport address was automatically as the pick up location, all the user had to specify was the destination address. The pickup and drop off address is then sent to the google geocoding api to be converted into longitude and lattitude coordinates. The coordinates were then sent to the Lyft api in in order to receive cost and ride time estimates for the ride. For dollar to skymile point conversions, it was assumed that $0.01 equaled one point. Once the user confirmed the ride, the skymile points were deducted from their account. We also tried to use the Lft api to create a simulated ride request but did not have enough time to implement it due to troubles with passing the proper parameters for that feature of the api. The user does not have to log in to their lyft account because it was assumed the ride was being purchased on delta's corporate lyft account. The entire app is responsive.

#API's
<ul>
	<li>Delta Customer api</li>
	<li>Google geocoding api</li>
	<li>Lyft api</li>
</ul>

#Contribution
<ul>
	<li><h2>Lawrence Chen</h2>
		<p>Helped write the front end. He did the moving cloud animation in the login animation (it's really suttle. Look at the very bottom of the page). He also photoshopped the background images to make them look perfect</p>
	</li>
	<li><h2>Forest Wong</h2>
	<p>Helped write the front end. He wrote most of the media queries to make the site responsive. It is important to not that this was Forest's first time working with html and css</p>
	</li>
	<li><h2>Jay Brooks</h2>
	<p>Wrote and populated the database. He helped geocode the destination for the lyft estimate (search) function. helped connect the controller to the database and helped write the sql queries for certain functions</p>
	</li>
	<li><h2>Mitchell Lee</h2>
	<p>Wrote the controller. Did most of the api communication. Got users from Delta api. Geocoded the origin airport and destination airport addresses using the google geocoding api. Got price and time estimates from the lyft api. </p>
	</li>
</ul>