<?php
$ch = curl_init();

$url = 'https://api.cratejoy.com/v1/shipments/711188561/';

curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE); 
curl_setopt($ch, CURLOPT_HEADER, FALSE); 
curl_setopt($ch, CURLOPT_USERPWD, 'client_id:client_secret'); 
curl_setopt($ch, CURLOPT_HTTPHEADER, array( 
    "Content-Type: application/json" 
));

$response = curl_exec($ch); 
curl_close($ch);
print "GET $url:\nResponse:\n";
var_dump($response);
print "\n";
?>
