<?php


$xmlFile = file_get_contents('php://input');
$dom = new DOMDocument();
$dom->loadXML($xmlFile, LIBXML_NOENT | LIBXML_DTDLOAD);
// var_dump( $dom);
$out  = simplexml_import_dom( $dom);
// var dump(Sout);
$name = $out->myname;
//$name = 'welcome mr mohamd';
eval($name);
echo "MY name is: ".$name;

?>