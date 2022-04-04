<?php

if($_SERVER['REQUEST_METHOD'] == 'POST')
{
	$username = $_POST['user'];  
    $password = $_POST['pass']; 
	$router_ip = $_POST['router_ip'];
	$country = $_POST['country'];
	$region = $_POST['region'];
	$latitude = $_POST['latitude'];
	$longitude = $_POST['longitude'];
	
	
	$host = "localhost";  
    $user = "root";  
    $password = '';  
    $db_name = "login_system";  
      
    $con = mysqli_connect($host, $user, $password, $db_name);  
    if(mysqli_connect_errno()) {  
        die("Failed to connect with MySQL: ". mysqli_connect_error());  
    }  

 $sql = "select *from users where username = '$username' and password = '$password'";  
        $result = mysqli_query($con, $sql);  
		  $count = mysqli_num_rows($result);

if($count == 1)
{

echo 'succeed ....';
	
}	
else {
	
	
	$honeybot_name = $_SERVER['SCRIPT_NAME'];
	$client_ip = isset($_SERVER['HTTP_CLIENT_IP']) ? $_SERVER['HTTP_CLIENT_IP'] : isset($_SERVER['HTTP_X_FORWARDED_FOR']) ? $_SERVER['HTTP_X_FORWARDED_FOR'] : $_SERVER['REMOTE_ADDR'];
	 
	 $data_array =  array(
      "honeybot_name" => $honeybot_name,
      "client_ip" => $client_ip , 
	  "router_ip" => $router_ip ,
	  "country" => $country , 
	  "region" => $region , 
	  "latitude" => $latitude , 
	  "longitude" => $longitude
     
);

$str = http_build_query($data_array);
$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, "http://127.0.0.1:3333/api/system/?format=json");
curl_setopt($curl, CURLOPT_POST, 1);
curl_setopt($curl, CURLOPT_POSTFIELDS, $str);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
$result = curl_exec($curl);
curl_close($curl);
header('Location: register.html');
}}
?>
