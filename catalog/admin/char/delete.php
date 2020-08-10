<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogChar.php';

$id = $SITE->d[5];

$CHAR = new AdminCatalogChar();
$catalog_id = $CHAR->delete($id);

header('location: /admin/com/catalog/char/'.$catalog_id);
exit;