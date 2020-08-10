<?php
defined('AUTH') or die('Restricted access');
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogChar.php';

$char['catalog_id'] = intval($_POST['catalog_id']);
$char['identifier'] = f_input('identifier');
$char['name'] = f_input('name');
$char['unit'] = f_input('unit');
$char['type'] = f_input('type');
$char['settings'] = '';
$char['ordering'] = intval($_POST['ordering']);

$CHAR = new AdminCatalogChar();
$CHAR->insert($char);

header('location: /admin/com/catalog/char/'.$char['catalog_id']);

function f_input($name){
	$post_data = isset($_POST[$name]) ? $_POST[$name] : '';
	return trim(htmlspecialchars(strip_tags($post_data)));
}
