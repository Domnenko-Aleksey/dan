<?php
defined('AUTH') or die('Restricted access');

switch ($SITE->d[4]){
	case 'add':
	case 'edit':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/char/edit.php';
		break;

	case 'delete':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/char/delete.php';
		break;

	case 'insert':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/char/insert.php';
		break;

	case 'ordering':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/char/ordering.php';
		break;
		
	case 'update':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/char/update.php';
		break;
	
	default:
		if (intval($SITE->d[4]) > 0) {
			// Если есть номер каталога - выводим его разделы
			include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/char/list.php';
			break;			
		} else {
			header("HTTP/1.0 404 Not Found");
			include "404.php";
			exit;
			break;
		}
}

?>