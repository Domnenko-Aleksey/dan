<?php
defined('AUTH') or die('Restricted access');

switch ($SITE->d[4]){
	case '':
	case 'add':
	case 'edit':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/item/edit.php';
		break;

	case 'delete':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/item/delete.php';
		break;

	case 'img_delete_ajax':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/item/img_delete_ajax.php';
		break;

	case 'img_upload_ajax':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/item/img_upload_ajax.php';
		break;

	case 'insert':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/item/insert.php';
		break;

	case 'pub':
	case 'unpub':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/item/pub.php';
		break;

	case 'settings_edit':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/item/settings_edit.php';
		break;

	case 'settings_update':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/item/settings_update.php';
		break;

	case 'up': case 'down':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/item/ordering.php';
		break;
		
	case 'update':
		include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/item/update.php';
		break;
	
	default:
		header("HTTP/1.0 404 Not Found");
		include "404.php";
		exit;
		break;
}

?>