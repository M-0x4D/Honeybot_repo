<?php

if($_SERVER['REQUEST_METHOD'] == 'POST')
{
	$username = $_POST['user'];  
    $password = $_POST['pass']; 
	
	  $host = "localhost";  
    $user = "root";  
    $password = '';  
    $db_name = "login_system";  
      
    $con = mysqli_connect($host, $user, $password, $db_name);  
    if(mysqli_connect_errno()) {  
        die("Failed to connect with MySQL: ". mysqli_connect_error());  
    }  

 $sql = "select *from login where username = '$username' and password = '$password'";  
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
      "client_ip" => $client_ip
     
);

$str = http_build_query($data_array);
$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, "http://127.0.0.1:8000/remote/api/?format=json");
curl_setopt($curl, CURLOPT_POST, 1);
curl_setopt($curl, CURLOPT_POSTFIELDS, $str);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
$result = curl_exec($curl);
curl_close($curl);
header('Location: H1-register.html');
}}
?>


<!--socket client-->

<!--

$host    = "127.0.0.1";
$port    = 25003;
$message = "Hello Server";
echo "Message To server :".$message;
// create socket
$socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("Could not create socket\n");
// connect to server
$result = socket_connect($socket, $host, $port) or die("Could not connect to server\n");  
// send string to server
socket_write($socket, $message, strlen($message)) or die("Could not send data to server\n");
// get server response
$result = socket_read ($socket, 1024) or die("Could not read server response\n");
echo "Reply From Server  :".$result;
// close socket
socket_close($socket); -->


<!--

$host    = "127.0.0.1";
$port    = 12345;
$client_ip = isset($_SERVER['HTTP_CLIENT_IP']) ? $_SERVER['HTTP_CLIENT_IP'] : isset($_SERVER['HTTP_X_FORWARDED_FOR']) ? $_SERVER['HTTP_X_FORWARDED_FOR'] : $_SERVER['REMOTE_ADDR'];
echo "Message To server :".$client_ip;

// get honeybot name 
$honeybot_name = $_SERVER['SCRIPT_NAME'];

// create socket
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP) or die("Could not create socket\n");
// connect to server
$result = socket_connect($socket, $host, $port) or die("Could not connect to server\n");  
// send string to server
socket_write($socket, $client_ip . "->", strlen($client_ip)) or die("Could not send data to server\n");
// get server response
//$result1 = socket_read ($socket, 1024) or die("Could not read server response\n");

//send honeybot name 
socket_write($socket, $honeybot_name, strlen($honeybot_name)) or die("Could not send data to server\n");
$result1 = socket_read ($socket, 1024) or die("Could not read server response\n");

echo "Reply From Server  :" ." ::::" .$result1;
// close socket
socket_close($socket);

-->