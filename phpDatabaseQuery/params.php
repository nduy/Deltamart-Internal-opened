<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
<?php
echo("<h1>XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</h1>")

?>

</body>
</html>

<?php
	require 'connection.php';


$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT CollectabilityID, ProviderID, Town, Location, Sensortype FROM collectability";
$result = $conn->query($sql);



if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
      
        echo "-->CollectabilityID: " . $row["CollectabilityID"]. " -| Town: " . $row["Town"]. "|Sensortype: " . $row["Sensortype"]. "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();
?>
</body>
</html>
