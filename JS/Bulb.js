<!DOCTYPE html>
<html>
<body>

<h2>What Can JavaScript Do?</h2>

<p>JavaScript can change HTML attribute values.</p>

<p>In this case JavaScript changes the value of the src (source) attribute of an image.</p>

<button onclick="document.getElementById('myImage').src='bulbon.gif'">Tekako</button>

<img id="myImage" src="bulboff.gif" style="width:100px">

<button onclick="document.getElementById('myImage').src='bulboff.gif'">Gyako</button>
</body>
</html>
