<?php
defined('AUTH') or die('Restricted access');

switch ($SITE->d[3]){
	case '': 
	case 'cat':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/cat/main.php';
		break;

	case 'char':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/char/main.php';
		break;

	case 'item':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/item/main.php';
		break;
	
	case 'section':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/section/main.php';
		break;
	
	default:
		header("HTTP/1.0 404 Not Found");
		include "404.php";
		exit;
		break;
}

?>