<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
<!--  <script type="text/javascript" src="scripts.js"></script> -->
<script src="scripts.js"></script>
  <title>Deltamart mini-prototype</title>
</head>
<body>
<?php
echo('<h1 style="text-align: center;"><strong><span style="color: #ff0000;"><span style="color: #0000ff;">DELTAMART</span></span></strong></h1>');
echo('<p style="text-align: center;"><span style="color: #800000;"><em><strong>MINI-PROTO</strong></em></span></p>');
?>

</body>
</html>

<?php
//$town="Galway";
	require 'connection.php';
  

$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
//Default values
$town= "Galway";
$location="Bedroom";
$sensortype= "HumiditySensor";
$providerid= "DDN";
if ($_GET['Town']!="")
$town =  $_GET['Town'];
if ($_GET['Location']!="")
 $location =  $_GET['Location'];
 if ($_GET['Sensortype']!="")
 $sensortype=  $_GET['Sensortype'];
 if ($$_GET['ProviderID']!="")
 $providerid=$_GET['ProviderID'];

echo("Hello town of  ".$town. "Location:".$location);
$sql = 'SELECT CollectabilityID, ProviderID, Town,TimeFrom,TimeTo,IoTDevice,ProviderIP, Location, Sensortype,TopicName,ZTNetworkID FROM collectability WHERE Town="'.$town
."\" AND Location=\"".$location. "\" AND Sensortype=\"".$sensortype. "\" AND ProviderID=\"".$providerid
.'"';
$result = $conn->query($sql);
echo("<br> DB QUERY:<br>".$sql."<br> <hr>");


if ($result->num_rows > 0) {
  // output data of each row
  $count=0;
  while($row = $result->fetch_assoc()) {
    $count=$count+1;
        echo "<===".$count."===><br>";
        echo "-->CollectabilityID: " . $row["CollectabilityID"]
        ."-| ProviderID: '" . $row["ProviderID"]
        ."| Sensor Type: '" . $row["Sensortype"]
        ."-| Town: '" . $row["Town"]
        ."-| Location: '" . $row["Location"]
        ."-| IoTDevice: '" . $row["IoTDevice"]
        ."-| A. From: '" . $row["TimeFrom"]
        ."-| A. To: '" . $row["TimeTo"]
        . "<br>"
          ."|Sensortype: " . $row["Sensortype"] 
          . "<span style=\"color:#006600\" onclick=\"alert('[  ProviderIP Adress]:". $row["ProviderIP"]."\\n[ZeroTier Network ID]:".$row["ZTNetworkID"].  "      \\n[MQTT Topic name  ]:   ".$row["TopicName"]."');\"><img alt=\"\" src=\"https://icons.iconarchive.com/icons/paomedia/small-n-flat/24/sign-info-icon.png\" style=\"height:24px; width:24px\" /></span>"

          .  "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();

?>
</body>
</html>
