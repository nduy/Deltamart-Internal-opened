<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
	"http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<title></title>
		<style> 
			.newspaper {
				-webkit-column-count: 3; /* Chrome, Safari, Opera */
				-moz-column-count: 3; /* Firefox */
				column-count: 3;
			}
		</style>
		<script src="jquery-1.11.3.min.js"></script>
		<script type="text/javascript" src="vis.js"></script>
		<link href="vis.css" rel="stylesheet" type="text/css" />
		 <style type="text/css">
			#mynetwork {
			  width: 100%;
			  height: 800px;
			  border: 1px solid lightgray;
			}
		</style>
		<script src="jquery-ui.js"></script>
		<script src="myjavascript.js"></script>
	</head>
	<body>
		<div id="mynetwork"></div>
		<div id="network_stats"></div>
		<button onclick="pause()">Start/Stop</button>
		<h1><br><br><br><br><br><br><br><br><br>Action log</h1>
		<div id="count_data"></div>
		<div id="return_data">Initializing...</div>
	</body>
</html>
