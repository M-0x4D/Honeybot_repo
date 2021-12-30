<?php 


if ($_SERVER['METHOD'] == 'POST')
{
	username = $_POST['uname'];
	password = $_POST['pass']
	
	
	$host = "localhost";  
    $user = "root";  
    $password = '';  
    $db_name = "login_system";  
      
    $con = mysqli_connect($host, $user, $password, $db_name);  
    if(mysqli_connect_errno()) {  
        die("Failed to connect with MySQL: ". mysqli_connect_error());  
		
		
		$sql = 'INSERT INTO login ("username" , "password") VALUES ('$username' , '$password')';
		$result = mysqli_query($con, $sql); 
		
    }  
}
?>