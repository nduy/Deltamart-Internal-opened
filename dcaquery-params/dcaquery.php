<?php

function conditionStr($arr) {
$res="";
$error_flag= false;
$count=0;
 foreach ($arr as $key => $value) {
//  echo("<br>COUNT=".$count);
//  echo("Values:".$key."=>".$value);
  if ($count!=0){
  if (in_array($key,["dcaID","data_type","ProviderID","BuyerID","PublisherReady","SubscriberReady","MQTTopic","UserID","Fullname","IPAddress","Email","Online","ZTNetworkID"])) {
  $res=$res." AND ".$key.'="'.$value.'"';
  } else{
    
  }
  $count=$count+1;
  
//  echo("<++>RES=|".$res."|");
  } else {
    # code...
     if (in_array($key,["dcaID","data_type","ProviderID","BuyerID","PublisherReady","SubscriberReady","MQTTopic","UserID","Fullname","IPAddress","Email","Online","ZTNetworkID"])) {
     $res=$res.$key.'="'.$value.'"';
     } else {
     
     }
     $count=$count+1;
  //   echo("<++>RES=|".$res."|");
  }
 }
  
 return $res; 
}
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

// echo "<br>* Condition".conditionStr($_GET);
if(array_key_exists("dcaID",$_GET))
  $dcaID = $_GET['dcaID'];

  /* Establish condtions
$Conditionstr="";  
foreach ($_GET as $key => $value) {
  echo "{$key} => {$value} ";
}
*/
//$sql = "SELECT * FROM	dcastatus JOIN Users ON dcastatus.ProviderID=Users.UserID WHERE".' dcaID= "'.$dcaID.'" AND ProviderID="FRE"';
//$sql = "SELECT dcaID,	data_type, ProviderID, BuyerID,	PublisherReady,SubscriberReady,MQTTopic FROM	dcastatus JOIN Users. ON dcastatus.ProviderID=Users.UserID  WHERE".' dcaID= "'.$dcaID.'"';
$sql = "SELECT * FROM	dcastatus JOIN Users ON dcastatus.ProviderID=Users.UserID WHERE ".conditionStr($_GET);
// echo("<br>QUERY: ".$sql);

$result = $conn->query($sql);
//echo(gettype($result));
//echo("<br> DB QUERY:<br>".$sql."<br> <hr>");
if(gettype($result)!="boolean")
{
  echo('{ "Response":"succeed","Count":'.$result->num_rows. ', "Results":[');
  

if ($result->num_rows > 0) {
  // output data of each row
  $count=0;
  //echo json_encode($result->fetch_assoc());
  while($row = $result->fetch_assoc()) {
    $count=$count+1;
  //  echo "<===".$count."===><br>";
    if ($count==1){//First item
      echo "".json_encode($row);
    }
    else{
      echo ",".json_encode($row);
    }
      
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
  //        . "<span style=\"color:#006600\" onclick=\"alert('[  ProviderIP Address]:". $row["ProviderIP"]."\\n[ZeroTier Network ID]:".$row["ZTNetworkID"].  "      \\n[MQTT Topic name  ]:   ".$row["TopicName"]."');\"><img alt=\"\" src=\"https://icons.iconarchive.com/icons/paomedia/small-n-flat/24/sign-info-icon.png\" style=\"height:24px; width:24px\" /></span>"

          .  "<br>"; */
          
  }
} else {
  echo "0 results";
}
}
$conn->close();
echo("]}");


?>
