<?php
$ch = curl_init();

$data = '{ 
    "status": "shipped", 
    "shipped_at": "2017-09-15", 
    "tracking_number": "123411" 
}';

$url = 'https://api.cratejoy.com/v1/shipments/711188561/';

curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE); 
curl_setopt($ch, CURLOPT_HEADER, FALSE); 
curl_setopt($ch, CURLOPT_USERPWD, 'my_client_id:my_secret_id'); 
curl_setopt($ch, CURLOPT_HTTPHEADER, array( 
    "Content-Type: application/json" 
));

curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT');
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);

$response = curl_exec($ch); 
curl_close($ch);
print "PUT $url:\n$data\n\n\nResponse:\n";
var_dump($response);
print "\n";
?>
