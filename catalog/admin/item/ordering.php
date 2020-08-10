<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogItem.php';
$ITEM = new AdminCatalogItem();

$arr['id'] = intval($SITE->d[5]);  // section id
$arr['type'] = $SITE->d[4];  // up / down

$section_id = $ITEM->getItem($arr['id'])['section_id'];

$ITEM->ordering($arr);

header('location: /admin/com/catalog/section/'.$section_id);
