<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogSection.php';
$SECTION = new AdminCatalogSection();

$arr['id'] = intval($SITE->d[5]);  // section id
$arr['type'] = $SITE->d[4];  // up / down

$catalog_id = $SECTION->getSection($arr['id'])['catalog_id'];

$SECTION->ordering($arr);

header('location: /admin/com/catalog/cat/'.$catalog_id);
