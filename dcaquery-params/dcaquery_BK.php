<!--
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script type="text/javascript" src="scripts.js"></script> 
<script src="scripts.js"></script>
-->
<!--  <title>Deltamart mini-prototype</title> 
</head>
<body>
<?php
//echo('<h1 style="text-align: center;"><strong><span style="color: #ff0000;"><span style="color: #0000ff;">DELTAMART</span></span></strong></h1>');
//echo('<p style="text-align: center;"><span style="color: #800000;"><em><strong>MINI-PROTO</strong></em></span></p>');
?>

</body>
</html>
-->
<?php
//$town="Galway";
	require 'connection.php';
  

$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
//Default values
$dcaID= "0ba99d92a3";
$sql = "";
echo json_encode($_GET);
if(array_key_exists("dcaID",$_GET))
  $dcaID = $_GET['dcaID'];
$sql = "SELECT * FROM	dcastatus WHERE".' dcaID= "'.$dcaID.'" AND ProviderID="FRE"';
//$sql = "SELECT dcaID,	data_type, ProviderID, BuyerID,	PublisherReady,SubscriberReady,MQTTopic FROM	dcastatus WHERE".' dcaID= "'.$dcaID.'"';
$result = $conn->query($sql);
echo("<br> DB QUERY:<br>".$sql."<br> <hr>");

echo( json_encode($result->fetch_assoc()));
if ($result->num_rows > 0) {
  // output data of each row
  $count=0;
  while($row = $result->fetch_assoc()) {
    $count=$count+1;
        echo "<===".$count."===><br>";
        echo json_encode($row);
  /*
        echo "-->dcaID: " . $row["dcaID"]
        ."-| data_type: '" . $row["data_type"]
        ."| ProviderID: '" . $row["ProviderID"]
        ."-| BuyerID: '" . $row["BuyerID"]
        ."-| PublisherReady: '" . $row["PublisherReady"]
        ."-| SubscriberReady: '" . $row["SubscriberReady"]
        ."-| MQTTopic: '" . $row["MQTTopic"]
  //      ."-| A. To: '" . $row["TimeTo"]
        . "<br>"
  //        ."|Sensortype: " . $row["Sensortype"] 
  //        . "<span style=\"color:#006600\" onclick=\"alert('[  ProviderIP Adress]:". $row["ProviderIP"]."\\n[ZeroTier Network ID]:".$row["ZTNetworkID"].  "      \\n[MQTT Topic name  ]:   ".$row["TopicName"]."');\"><img alt=\"\" src=\"https://icons.iconarchive.com/icons/paomedia/small-n-flat/24/sign-info-icon.png\" style=\"height:24px; width:24px\" /></span>"

          .  "<br>"; */
  }
} else {
  echo "0 results";
}
$conn->close();

?>
</body>
</html>
