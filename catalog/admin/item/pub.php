<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogItem.php';
$ITEM = new AdminCatalogItem();

$arr['id'] = intval($SITE->d[5]);  // item id
$arr['pub'] = $SITE->d[4] == 'pub' ? 1 : 0;  // pub / unpub

$section_id = $ITEM->getItem($arr['id'])['section_id'];

$ITEM->pub_unpub($arr);

header('location: /admin/com/catalog/section/'.$section_id);
