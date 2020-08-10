<?php
defined('AUTH') or die('Restricted access');

switch ($SITE->d[4]){
	case 'list':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/section/mainpage.php';
		break;

	case 'add':
	case 'edit':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/section/edit.php';
		break;

	case 'delete':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/section/delete.php';
		break;

	case 'insert':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/section/insert.php';
		break;

	case 'pub':
	case 'unpub':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/section/pub.php';
		break;

	case 'settings_edit':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/section/settings_edit.php';
		break;

	case 'settings_update':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/section/settings_update.php';
		break;

	case 'up': case 'down':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/section/ordering.php';
		break;
		
	case 'update':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/section/update.php';
		break;
	
	default:
		if (intval($SITE->d[4]) > 0) {
			// Если есть номер каталога - выводим его разделы
			include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/section/items.php';
			break;			
		} else {
			header("HTTP/1.0 404 Not Found");
			include "404.php";
			exit;
			break;
		}
}

?>