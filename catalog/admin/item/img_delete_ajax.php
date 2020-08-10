<?php
defined('AUTH') or die('Restricted access');
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogItem.php';
$ITEM = new AdminCatalogItem();

$id = intval($_POST['id']);
$file_name = trim(htmlspecialchars(strip_tags($_POST['file_name'])));

$item = $ITEM->getItem($id);

$s = '/'.$file_name.'[;]?/';
$item['images'] = preg_replace ($s, '', $item['images']);

$ITEM->updateImages($item);

$catalog = $ITEM->getCatalogByItemId($id);
$file = $_SERVER['DOCUMENT_ROOT'].'/files/catalog/'.$catalog['id'].'/items/'.$file_name;
if (is_file($file))
	unlink($file);

echo json_encode(array('answer' => 'success'));
exit;